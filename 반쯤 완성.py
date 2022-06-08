import requests, csv, time, tkinter
from urllib import parse
from datetime import datetime
from bs4 import BeautifulSoup
from selenium import webdriver
from encodings import utf_8
from datetime import datetime
from tkinter import ttk


class SampleApp(tkinter.Tk):
    def __init__(window):
        tkinter.Tk.__init__(window)
        window.title("자가진단")
        window.geometry("290x210")#("260x210") #가로 세로 x좌표이동 y좌표이동
        window.resizable(False,False) #xy좌표변경안됨
        window._frame = None
        window.switch_frame(StartPage)

    def switch_frame(window, frame_class):
        new_frame = frame_class(window)
        if window._frame is not None:
            window._frame.destroy()
        window._frame = new_frame
        window._frame.pack()

#처음 프레임 코드
class StartPage(tkinter.Frame):
    def __init__(window, master):
        infocsv = open('./info.csv', 'r', encoding="utf-8") #파일이 있는 경로+파일이름.csv
        value_csv1 = csv.reader(infocsv)
        csv_info=[]
        for value_csv2 in value_csv1 :
            csv_info.append(value_csv2)
        start_time, user_name, user_birthday ,user_password = tkinter.StringVar(),tkinter.StringVar(), tkinter.StringVar(), tkinter.StringVar()
        start_time.set(csv_info[0]),user_name.set(csv_info[1]), user_birthday.set(csv_info[2]), user_password.set(csv_info[3])
        #입력한 데이터와 저장된 데이터를 비교하는 함수 
        def data_check():
            if '['+start_time.get()[1:-2]+']' == str(csv_info[0]) and '['+user_name.get()[1:-2]+']' == str(csv_info[1]) and '['+user_birthday.get()[1:-2]+']' == str(csv_info[2]) and '['+user_password.get()[1:-2]+']' == str(csv_info[3]):
                master.switch_frame(SamePage)
            else:
                #csv_save=[str(start_time.get()),str(user_name.get()),str(user_birthday.get()),str(user_password.get())]
                
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
                time.sleep(1)
                
                #프레임 변경 코드
                master.switch_frame(SamePage)
                #master.switch_frame(DifferentPage)
        
        tkinter.Frame.__init__(window, master)
        ttk.Label(window, text = "실행 시간" ).grid(row = 0, column = 0, padx = 10, pady = 10)
        ttk.Label(window, text = "이름" ).grid(row = 1, column = 0, padx = 10, pady = 10)
        ttk.Label(window, text = "생년월일").grid(row = 2, column = 0, padx = 10, pady = 10)
        ttk.Label(window, text = "비밀번호").grid(row = 3, column = 0, padx = 10, pady = 10)
        ttk.Entry(window, textvariable = start_time).grid(row = 0, column = 1, padx = 10, pady = 10)
        ttk.Entry(window, textvariable = user_name).grid(row = 1, column = 1, padx = 10, pady = 10)
        ttk.Entry(window, textvariable = user_birthday).grid(row = 2, column = 1, padx = 10, pady = 10)
        ttk.Entry(window, textvariable = user_password, show='*').grid(row = 3, column = 1, padx = 10, pady = 10)
        ttk.Button(window, text = "시작", command = data_check).grid(row = 4, column = 1, padx = 10, pady = 10)

#정보가 다를 경우의 프레임
#하지만 지금은 안됨
class DifferentPage(tkinter.Frame):
    def __init__(window, master):
        tkinter.Frame.__init__(window, master)
        ttk.Label(window, text = " " ).grid(row = 0, column = 0, padx = 10, pady = 10)
        ttk.Label(window, text = " 정보가 다릅니다." ).grid(row = 1, column = 0, padx = 10, pady = 10)
        ttk.Label(window, text = "입력된 정보를 저장하고 실행 하시겠습니까?").grid(row = 2, column = 0, padx = 10, pady = 10)
        ttk.Label(window, text = " ").grid(row = 3, column = 0, padx = 10, pady = 10)
        ttk.Button(window, text= "취소", command =lambda: master.switch_frame(StartPage)).grid(row = 4, column = 0, padx = 10, pady = 10)
        ttk.Label(window, text = " ").grid(row = 0, column = 1, padx = 10, pady = 10)
        ttk.Label(window, text = " ").grid(row = 1, column = 1, padx = 10, pady = 10)
        ttk.Label(window, text = " ").grid(row = 2, column = 1, padx = 10, pady = 10)
        ttk.Label(window, text = " ").grid(row = 3, column = 1, padx = 10, pady = 10)
        ttk.Button(window, text= "저장&실행", command=lambda: master.switch_frame(SamePage)).grid(row = 4, column = 1, padx = 10, pady = 10)

#시작된 프레임
class SamePage(tkinter.Frame):
    def __init__(window, master):
        tkinter.Frame.__init__(window, master)
        #자가진단 함수
        def jagajindan():

            #휴일 정보 api
            def dayoff():
                if int(datetime.today().strftime('%w')) == 0 or int(datetime.today().strftime('%w')) == 6:
                    print('휴일')
                    return True
                else:
                    url = "http://apis.data.go.kr/B090041/openapi/service/SpcdeInfoService/getRestDeInfo"
                    api_key_utf8 = "ZwivLrudvl%2FhrxYMBlaZ6xvtJedAxNHKtdER0N6vGRidDZEeM4yup%2BqB2VH9S9%2BcAhUdBSxqULAmTX7ZvvLuoA%3D%3D"
                    api_key_decode = parse.unquote(api_key_utf8)
                    params = {
                        "ServiceKey": api_key_decode,
                        "solYear": datetime.today().year,
                        "numOfRows": 100,
                        "solMonth": datetime.today().strftime('%m')
                    }
                    response = requests.get(url, params=params)
                    time.sleep(2)
                    xml = BeautifulSoup(response.text, "lxml")
                    time.sleep(2)
                    print(xml)
                    items = xml.find('items')
                    item_list = []
                    for item in items:
                        item_list.append(item.find("locdate").get_text())
                    for item in item_list:
                        if int(item) == int(datetime.today().strftime("%Y%m%d")):
                            print('휴일')
                            return True
                return False

            #비밀번호 해독을 위한 함수
            def userpassword():
                p1 = driver.find_element_by_xpath('//*[@id="password_mainDiv"]/div[4]/a')
                p2 = driver.find_element_by_xpath('//*[@id="password_mainDiv"]/div[5]/a[1]')
                p3 = driver.find_element_by_xpath('//*[@id="password_mainDiv"]/div[5]/a[2]')
                p4 = driver.find_element_by_xpath('//*[@id="password_mainDiv"]/div[5]/a[3]')
                p5 = driver.find_element_by_xpath('//*[@id="password_mainDiv"]/div[5]/a[4]')
                p6 = driver.find_element_by_xpath('//*[@id="password_mainDiv"]/div[6]/a')
                p7 = driver.find_element_by_xpath('//*[@id="password_mainDiv"]/div[7]/a')
                p8 = driver.find_element_by_xpath('//*[@id="password_mainDiv"]/div[8]/a[1]')
                p9 = driver.find_element_by_xpath('//*[@id="password_mainDiv"]/div[8]/a[2]')
                p10 = driver.find_element_by_xpath('//*[@id="password_mainDiv"]/div[8]/a[3]')
                p11 = driver.find_element_by_xpath('//*[@id="password_mainDiv"]/div[8]/a[4]')
                p12 = driver.find_element_by_xpath('//*[@id="password_mainDiv"]/div[9]/a')
                #비밀번호 위치를 리스트로 변환?저장?
                password = [p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12]
                # 현재 html을 soup에 저장
                soup = BeautifulSoup(driver.page_source, 'html.parser')
                # l 이라는 list에 현재 비밀번호 각각의 위치 저장
                l=[]
                for i in range(1+4,12+4+1):
                    l.append(soup.select('a')[i]['aria-label'])
                # 지정된 번호와 현재 비밀번호 위치를 비교하여
                # 지정된 숫자가 있는 위치의 순서를 반환하여 그 위치를 클릭 하는 함수
                def Choosepassword(c):
                    #함수를 쓰기위한 0 ~ 9 까지의 리스트
                    num09=['0','1','2','3','4','5','6','7','8','9']
                    for j in range(c,12+1):
                        if l[j]==num09[c]:
                            password[j].click()
                            print(j)
                            break
                #비밀번호
                Choosepassword(int(user_password[:1]))
                Choosepassword(int(user_password[1:2]))
                Choosepassword(int(user_password[2:3]))
                Choosepassword(int(user_password[3:4]))
            
            if dayoff() == False:#True
                webdriver_options = webdriver.ChromeOptions()
                #webdriver_options.add_argument('headless')
                #webdriver_options.add_argument('windows-size=1920x1080')
                #webdriver_options.add_argument('disable-gpu')
                driver = webdriver.Chrome( 'chromedriver.exe', options =  webdriver_options )
                url = 'https://hcs.eduro.go.kr/#/loginHome'
                driver.get(url)
                time.sleep(2)
                #자가진단 참여하기
                driver.find_element_by_xpath('//*[@id="btnConfirm2"]').click()
                #학교 검색
                driver.find_element_by_xpath('//*[@id="schul_name_input"]').click()
                #시/도 (충청남도) 선택
                driver.find_element_by_xpath('//*[@id="sidolabel"]/option[13]').click()
                #고등학교 선택
                driver.find_element_by_xpath('//*[@id="crseScCode"]/option[5]').click()
                #금산고등학교 입력
                driver.find_element_by_xpath('//*[@id="orgname"]').send_keys('금산고등학교')
                #검색
                driver.find_element_by_xpath('//*[@id="softBoardListLayer"]/div[2]/div[1]/table/tbody/tr[3]/td[2]/button').click()
                #웹 불러오기 서버로 인한 일시정지
                time.sleep(1)
                #li 중 금산고등학교 선택
                driver.find_element_by_xpath("//*[@id='softBoardListLayer']/div[2]/div[1]/ul/li/a").click()
                #학교선택
                driver.find_element_by_xpath('//*[@id="softBoardListLayer"]/div[2]/div[2]/input').click()
                #성명 입력
                driver.find_element_by_xpath('//*[@id="user_name_input"]').send_keys(str(user_name))
                #생년월일 입력
                driver.find_element_by_xpath('//*[@id="birthday_input"]').send_keys(str(user_birthday))
                #확인 없어졌나봄
                #driver.find_element_by_xpath('//*[@id="btnConfirm"]').click()
                #여기도 가끔 오류남
                time.sleep(1)
                # driver.implicitly_wait(10) ## 암묵적으로 웹 자원을 (최대) 10초 기다리기 # 이거 아닌가봄
                #보안 키패드 클릭
                driver.find_element_by_xpath('//*[@id="WriteInfoForm"]/table/tbody/tr[4]/td/div/button').click()
                #여기는 체크하지 않음
                time.sleep(1)
                userpassword()
                #userpassword(user_password[:1],user_password[1:2],user_password[2:3],user_password[3:4])
                #비밀번호 확인
                driver.find_element_by_xpath('//*[@id="btnConfirm"]').click()
                #오류로 인한 일시정지
                time.sleep(3)
                #계정 선택 (미참여 인거)
                driver.find_element_by_xpath('//*[@id="container"]/div/section[2]/div[2]/ul/li/a[1]').click()
                #문제생김 일시정지
                time.sleep(1)
                # 1. 임상증상 아니요
                driver.find_element_by_xpath('//*[@id="survey_q1a1"]').click()
                # 2. 신속항원검사 검사하지 않음
                driver.find_element_by_xpath('//*[@id="survey_q2a3"]').click()
                # 2-1. 신속항원검사 음성 (월,수)
                #driver.find_element_by_xpath('//*[@id="survey_q2a1"]').click()
                # 3. 본인 또는 동거인 PCR검사결과 기다리고 있니요? 아니요
                driver.find_element_by_xpath('//*[@id="survey_q3a1"]').click()
                #제출
                driver.find_element_by_xpath('//*[@id="btnConfirm"]').click()
                time.sleep(2)
                #브라우저 종료
                driver.quit()

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
        print(start_time, user_name, user_birthday ,user_password)

        # 무한반복을 구현할 지점? 함수? 
        condition = True
        def infinite_loop():
            if condition:
                jagajindan_start = 0
                if int(time.strftime('%H', time.localtime(time.time()))) == int(start_time[:-3]) and int(time.strftime('%M', time.localtime(time.time()))) == int(start_time[3:]) :
                    jagajindan()
                    print(datetime.now())
                    jagajindan_start = 1  
                #print(int(time.strftime('%H', time.localtime(time.time()))),int(start_time[:-3]),int(time.strftime('%M', time.localtime(time.time()))), int(start_time[3:]))
                if jagajindan_start == 0:
                    print('1초')
                    #밑의 코드는 ms 단위로 몇초 뒤에 함수를 시작함
                    window.after(1000, infinite_loop)
                if jagajindan_start == 1:
                    print('86380초')
                    window.after(86380000, infinite_loop)

        #무한반복을 시작, 정지할 함수
        def start():
            global condition
            condition=True
            infinite_loop()
        def stop():
            global condition
            condition=False
            master.switch_frame(StartPage)

        #함수를 따로 시작 해주어야 함.
        start()

        ttk.Label(window, text = " ").grid(row = 0, column = 0, padx = 10, pady = 10)
        ttk.Label(window, text = str(start_time)+' 에 실행됩니다.', font=('Arial', 12, "bold")).grid(row = 1, column = 0, columnspan = 2, padx = 10, pady = 10)
        ttk.Label(window, text = " ").grid(row = 2, column = 0, padx = 10, pady = 10)
        ttk.Label(window, text = " ").grid(row = 3, column = 0, padx = 10, pady = 10)
        ttk.Button(window, text= "중지", command = stop).grid(row = 4, column = 0, padx = 10, pady = 10)
        ttk.Label(window, text = " ").grid(row = 0, column = 1, padx = 10, pady = 10)
        #ttk.Label(window, text = " ").grid(row = 1, column = 1, padx = 10, pady = 10)
        ttk.Label(window, text = " ").grid(row = 2, column = 1, padx = 10, pady = 10)
        ttk.Label(window, text = " ").grid(row = 3, column = 1, padx = 10, pady = 10)
        ttk.Button(window, text= "종료", command = window.quit).grid(row = 4, column = 1, padx = 10, pady = 10)
        
if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()