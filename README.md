기본설정|(기본값)|
---|---|
실행시간|08:00 (24시 기준)|
이름|심화섭|
생년월일|000000 (주민등록번호 앞자리)|
비밀번호|0000|
   
[자가진단 자동화.py](https://github.com/SimHwaseop/auto-jagajindan/blob/master/%EB%B0%98%EC%AF%A4%20%EC%99%84%EC%84%B1.py)

파이썬을 이용하여 개발하였고, 파이썬으로 가장 많이 사용한 것은 Selenium과 BeautifulSoup이고 Selenium은 웹 사이트를 접속하여 정보를 크롤링하거나 웹사이트를 사용자처럼 둔갑하여 기능을 자동화하여 사용할 수 있는 모듈(라이브러리)이고, BeautifulSoup은 requests을 이용하여 웹사이트나 api등에 접속하여 정보를 크롤링할 수 있는 모듈이다.

## Selenium을 활용한 자가진단 자동화 프로그램 개발 보고서
#### 배경
교육부에서 시행한 '건강상태자가진단'은 시행할 때부터 학생들의 의문, 그러니까 사용시에 일어나는 효과가미미하거나 없다는 의문이 제기 되었고, 또 다른 문제인 반에서 '건강상태자가진단'을 하지 않을 시에 휴대전화를 압수하는 규칙이 생겨난 뒤로 이 프로그램을 만들어야겠다는 확신이 어들 만들게됨 .
      
#### 개발과정 (오류해결과정)
유튜브에서 크롤링 관련 영상들의 보다가 Selenium을 알게 되었고 이 것으로 만들게됨.  
개발환경은 Visual Studio Code를 이용했으며, Python언어를 사용하여 개발함.  
처음 Selenium을 활용하여 개발을 할때에 Xpath를 사용하여 호출하는 방식으로 사용하였고, 그 중 첫 번째 오류로
```error
no such element: Unable to locate element:
```
위의 오류가 반환되었고 이 것을 찾아보니 검색으로는 나오지 않았고, 뜻이 엘리멘트가 없다는 뜻인 것 같아 이 오류가 생긴 코드 앞줄에 일시정지 코드(아래) 넣에서 첫 번째 문제는 해결됨.
```py
time.sleep(1)
```
  
2번쨰로 보안 키패드 문제를 해결하기 위해서는 처음으로는 비밀번호 숫자 엘리멘트들의 위치 12개(빈것2개와 0~9)를 일단 찾아 저장하고, 그 다음으로는 어떠한 태그의 어떠한 속성을 가진 것의 속성 변수를 불러오기 위하여 BeautifulSoup를 사용했다.
```py
soup = BeautifulSoup(driver.page_source, 'html.parser')
```
위 코드방식으로 셀레니움으로 실행중인 의창 html을 파섹하여 soup라는 변수에 저장하고, 
```py
l=[]
    for i in range(1+4,12+4+1):
        l.append(soup.select('a')[i]['aria-label'])
```
위의 코드방식으로 soup라는 변수 안에 a태그안에 aria-label이라는 속성이 있는 i번쨰 값을 불러와 l이라는 리스트 변수에 저장하는 방식으로 비밀번호 키패드의 위치를 크롤링함. (aria-label속성은 보통 보여지는 값을 속성으로 해놓은 것이라고 함.)
이후 숫자를 비교해 맞는 위치의 엘리멘트를 클릭하도록 구현함.  
  
이 후 휴일은 자가진단이 자동으로 되지 않아야 하기 떄문에 공공 데이터 포털의 ‘한국 천문연구원_특일 정보’ 라는 오픈 api를 이용하여 대한민국을 공휴일 ex)지방선거일, 현충일 등의 평일의 공휴일을 불러와 그날에는 실행되지 않도록 하였다.  
  
이 프로그램을 사용자가 사용하기 위해서는 파이썬 형태의 파일이 아닌 사용자가 사용하기 편하도록 하는 인터페이스가 필요하다고 생각되어 웹서버 형태로 인터넷 창으로 관리를 할지와 그냥 프로그램 창으로 하는 형태 2가지로 고민과 검색으로 찾아보다가 웹 형식은 아직 배우지 못해서 구현이 어렵다고 판단하여 그냥 프로그램 형식으로 만드는 결론을 내였다. 일반적인 프로그램 gui창을 구현하기 위해서는 파이썬의 'Tkinter'라는 모듈을 사용하였다.  
  
Tkinter 는 아래와 같이  
```py
window=tkinter.Tk()

window.mainloop()
```
두 개의 코드 사이에서 코드를 작성하여야 하고,  
```py
window.title("자가진단")
window.geometry("245x210")#("260x210") #가로 세로 x좌표이동 y좌표이동
window.resizable(False,False) #xy좌표변경안됨
```
위와 같이 타이틀과 창의 크기, 창의 형태를 사용자가 변환할 수 있을지의 유무 등과 같은 변수들을 설정 할 수 있다.  
```py
window = tkinter.Tk()
```
위 코드의 예제를 보고서  '굳이 변수안에 tkinter.Tk()를 넣어야 할까?‘ 라는 생각을 한뒤에 변수를 만들지 않고서 그냥 tkinter.Tk()로 선언 하고서 프로그램을 실행하였더니 한 형태(Label, Button 등) 들이 각각 독립된 형태로 실행되는 아주 재밌는 오류가 생기는 것을 확인하게 됨.  
  
tkinter를 이용하여 gui를 만들 때 ttk와 tk가 있다. ttk 확장모듈은 tk의 그래픽의 각진 형태에서 더 보기 좋은 형태로 변화 시켜준다는 특징이 있다.
그래서 ttk를 이용하여 gui를 구현 했다.  
```py
ttk.Label(window, text = " " ).grid(row = 0, column = 0, padx = 10, pady = 10)
```
위의 코드에서처럼 그리드의 row는 열의 위치를 나타내고, column은 해의 위치를 나타내며 pady,padx는 픽셀 값이다. 이외에도 columnspan은 행을 합치는 속성이다. ex) columnspan = 2 는 옆에 있는 행 1개와 합친다는 뜻이다.  
  
그 다음으로 가장 중요한 오류로는 tkinter에서는 반복문(for, while) 이 실행되면 프레임 전환이 되지 않으며, gui창이 조작 할 수 없는 상태로 반복문이 계속 실행되고 있어 프로그램을 종료해야 꺼지기 때문이다. 이 문제를 해결하기 위해서 구글링을 하였고 예시코드를 찾았다.(아래 코드)
```py
# Import the required library
from tkinter import *

# Create an instance of tkinter frame
win=Tk()

# Set the size of the Tkinter window
win.geometry("700x350")

# Define a function to print something inside infinite loop
condition=True
def infinite_loop():
   if condition:
      Label(win, text="Infinite Loop!", font="Arial, 25").pack()

   # Call the infinite_loop() again after 1 sec win.after(1000, infinite_loop)

def start():
   global condition
   condition=True

def stop():
   global condition
   condition=False

# Create a button to start the infinite loop
start = Button(win, text= "Start the Loop", font="Arial, 12", command=start).pack()
stop = Button(win, text="Stop the Loop", font="Arial, 12", command=stop).pack()

# Call the infinite_loop function after 1 sec.
win.after(1000, infinite_loop)

win.mainloop()
```
위의 예제를 찾았는데 위의 코드는 버튼을 눌러도 반응이 없었기 떄문에 문제가 있다고 판단후 다른 예제를 찾기 위해 구글링을 하였지만, 다른 예제를 찾지는 못하였고 이예제를 보고 있으니 밑의 코드인
```py
win.after(1000, infinite_loop)
```
위의 코드를 위치를 바꾸는 방식으로 아래와 같이 코드를 변경하였더니
```py
# Import the required library
from tkinter import *

# Create an instance of tkinter frame
win=Tk()

# Set the size of the Tkinter window
win.geometry("700x350")

# Define a function to print something inside infinite loop
condition=True
def infinite_loop():
   if condition:
      Label(win, text="Infinite Loop!", font="Arial, 25").pack()
      win.after(1000, infinite_loop)

   # Call the infinite_loop() again after 1 sec win.after(1000, infinite_loop)

def start():
   global condition
   condition=True
   infinite_loop()

def stop():
   global condition
   condition=False

# Create a button to start the infinite loop
start = Button(win, text= "Start the Loop", font="Arial, 12", command=start).pack()
stop = Button(win, text="Stop the Loop", font="Arial, 12", command=stop).pack()

# Call the infinite_loop function after 1 sec.


win.mainloop()
```
정상적으로 무한루프 프로그램이 되었기 떄문에 위의 코드를 참고하여 무한 루프를 구현 하였다.  
  
이것을 만든 뒤에 사용자 정보를 저장하기 위해서는 어떤 방법이 있을지 고민하다가 CSV 파일을 이용하여 사용자 정보를 저장하고 프로그램이 실행될 떄 불러오고 변경되면 저장하는 방식으로 계획하였고 그렇게 구현하였다.  

```py
#이런 형태인 이유는 오류가 생겼기 때문
#처음에 csv 파일을 초기화 한 다음 저장 후 추가하는 형태
with open("info.csv", 'w') as f:
  if str(start_time.get()).startswith('('):
     f.write(str(start_time.get()[2:-3]))
     f.close
  else:
     f.write(str(start_time.get()))
     f.close
with open("info.csv", 'a', newline='',encoding = "utf-8") as f:
  if str(user_name.get()).startswith('('):
     f.write('\n'+str(user_name.get()[2:-3]))
     f.close
  else:
     f.write('\n'+str(user_name.get()))
     f.close
with open("info.csv", 'a') as f:
  if str(user_birthday.get()).startswith('('):
     f.write('\n'+str(user_birthday.get()[2:-3]))
     f.close
  else:
     f.write('\n'+str(user_birthday.get()))
     f.close
with open("info.csv", 'a') as f:
  if str(user_password.get()).startswith('('):
     f.write('\n'+str(user_password.get()[2:-3]))
     f.close
  else:
     f.write('\n'+str(user_password.get()))
     f.close


#csv 파일에서 사용자 정보를 불러오기
infocsv = open('./info.csv',  encoding="utf-8") #파일이 있는 경로+파일이름.csv
value_csv1 = csv.reader(infocsv)
csv_info=[]
for value_csv2 in value_csv1 :
   csv_info.append(value_csv2)
start_time =  str(csv_info[0])[2:-2]
user_name = str(csv_info[1])[2:-2]
user_birthday = str(csv_info[2])[2:-2]
user_password = str(csv_info[3])[2:-2]
```
위의 코드로 구현한 이유는 짧은 코드로는 문제가 생겨 위 처럼 처음에 새로운 피일로 저장하고 그뒤의 내용을 추가하는 형태로 저장하도록 구현하였고, 그 밑의 코드는 CSV파일의 사용자 정보를 불러오기 위해서 사용한 코드이다.  
    
이 프로그램은 제목 그대로가 설명이듯이 자가 진단을 자동화하는 기능만을 가지고 있다. 
자가 진단은 교육부의 방역 정책이지만 실효성이 없다고 판단하여 만들었지만 프로그램은 내가 만든 것이 아니더라도 유튜브 등에서 아이폰의 단축어를 이용하는 것도 있고, 자동화하는 코딩을 한 영상도 존재한다. 하지만 이것을 보고서 사용하는 것은 모두가 똑같은 경험을 줄 수 있을지는 몰라도 이 프로그램을 만드는 것은 다른 의미가 있다고 생각한다. 이 프로그램을 만들면서 웹사이트의 형태나 원리 등을 알아보고 그것을 통해서 프로그램을 개발하면서 웹사이트의 형태와 원리를 알 수 있었고 그것이 아니라도 이 프로그램을 GUI를 만들기 위해서 tinter를 사용하였는데 그것을 통해 tinter에서의 오류 또한 해보지 않으면 경험할 수 없는 것이기 때문에 프로그램을 만들면서 알게 된 오류들을 해결한 방법들의 경험을 얻은 것이고 만들지 않고도 프로그램은 사용할 수 있지만 프로그램을 만들어 봄으로써 프로그램의 원리를 알 수 있었다. 그리고 주제가 “자가진단 자동화”라서 그렇지 이 프로잭트를 통해서 얻는 경험과 정보들은 다른 크롤링이 필요한 프로그램에서 사용할 수 있기 때문에 의미가 있다고 생각한다.
또한 이 프로젝트에서 더 발전시켜 원래의 정보와 다른 정보를 입력한다면 경고창으로 바꾸는 것을 시도하였지만 변수를 다른 클래스에서 사용하는 방법을 찾지 못해 실패하였지만 찾는다면 원하는 방향대로 만들 수 있고, 다른 방법으로 정보를 다른 파일로 저장하고 정보를 사용자의 선택에 따라 바꾸거나 삭제하는 방향으로 만들 수도 있을 것으로 예상된다.
그리고 이 프로그램과 중심이 되는 코드만을 이용해서 리눅스를 사용하는 서버에서 프로그램을 실행하여 실제 자동화 서버로 이용할 수 있다고 생각하여 실제로 리눅스 서버에서 사용 중이다. 그리고 다른 프로젝트를 하면서 디스코드를 이용한 알림을 알게 되었는데 이것을 통하여 리눅스 서버에서 사용중인 프로그램에서 오류가 발생하는 빈도가 많아서 구동이 되는지를 디스코드로 알림을 통해 로그를 남기는 것을 응용하여 만들어 사용하고 있다. 그리고 이 문서와 프로젝트 파일들을 훨씬 더 편리하게 이용하기 위하여 깃허브를 이용해 프로그램 파일과 설명 문서를 업로드하여 사용하고 있다. [GITHUB](https://github.com/SimHwaseop/auto-jagajindan)
