import requests,time,csv
from urllib import parse
from datetime import datetime
from bs4 import BeautifulSoup
from selenium import webdriver
#휴일 정보 불러오는 거
def dayoff():
    if int(datetime.today().strftime('%w')) == 0 or int(datetime.today().strftime('%w')) == 6:
        return True
    #elif int(datetime.today().strftime('%w')) == 6:
    #    return True
    else:
        url = "http://apis.data.go.kr/B090041/openapi/service/SpcdeInfoService/getRestDeInfo?ServiceKey=ZwivLrudvl%2FhrxYMBlaZ6xvtJedAxNHKtdER0N6vGRidDZEeM4yup%2BqB2VH9S9%2BcAhUdBSxqULAmTX7ZvvLuoA%3D%3D"+"&solYear="+str(datetime.today().year)+"&solMonth="+str(datetime.today().strftime('%m'))
        print(url)
        response = requests.get(url)
        xml = BeautifulSoup(response.text, "lxml")
        items = xml.find('items')
        item_list = []
        for item in items:
            item_list.append(item.find("locdate").get_text())
    
        for item in item_list:
            if int(item) == int(datetime.today().strftime("%Y%m%d")):
                return True
    return False
def userpassword(up1,up2,up3,up4):
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
    # 지정된 숫자가 있는 위치의 순서를 반환하여 그 위치를 클릭 함 
    def Choosepassword(c):
        #함수를 쓰기위한 0 ~ 9 까지의 리스트
        num09=['0','1','2','3','4','5','6','7','8','9']
        for j in range(c,12+1):
            if l[j]==num09[c]:
                password[j].click()
                #print()
                print(j)
                #print()
                break
    #비밀번호
    Choosepassword(int(up1))
    Choosepassword(int(up2))
    Choosepassword(int(up3))
    Choosepassword(int(up4))



if dayoff() == False: #True    
    #밑의 링크 헤드리스 설명
    #http://afrobambacar.github.io/2016/03/%EB%88%88%EC%97%90-%EB%B3%B4%EC%9D%B4%EC%A7%80-%EC%95%8A%EB%8A%94-%EB%B8%8C%EB%9D%BC%EC%9A%B0%EC%A0%80-phantomjs.html
    webdriver_options = webdriver.ChromeOptions()
    webdriver_options.add_argument('headless')
    webdriver_options.add_argument('windows-size=1920x1080')
    webdriver_options.add_argument('disable-gpu')
    #webdriver_options.add_arguemnt('User-Agent:')
    #webdriver_options.add_arguemnt('lang=ko_KR')
    driver = webdriver.Chrome('auto-jagajindan_linux64/chromedriver', options =  webdriver_options )
    url = 'https://hcs.eduro.go.kr/#/loginHome'
    driver.get(url)
    #print('사이트 실행')
    #자가진단 참여하기
    driver.find_element_by_xpath('//*[@id="btnConfirm2"]').click()
    #print('자가진단 참여 클릭')
    #학교 검색
    driver.find_element_by_xpath('//*[@id="schul_name_input"]').click()
    #print('학교 검색 클릭')
    #시/도 (충청남도) 선택
    driver.find_element_by_xpath('//*[@id="sidolabel"]/option[13]').click()
    #print('충청남도 선택')
    #고등학교 선택
    driver.find_element_by_xpath('//*[@id="crseScCode"]/option[5]').click()
    #print('고등학교 클릭')
    #금산고등학교 입력
    driver.find_element_by_xpath('//*[@id="orgname"]').send_keys('금산고등학교')
    #print('금산고등학교 입력')
    #검색
    driver.find_element_by_xpath('//*[@id="softBoardListLayer"]/div[2]/div[1]/table/tbody/tr[3]/td[2]/button').click()
    #print('고등학교 검색중...')
    #웹 불러오기 서버로 인한 일시정지
    time.sleep(1)
    #li 중 금산고등학교 선택
    driver.find_element_by_xpath("//*[@id='softBoardListLayer']/div[2]/div[1]/ul/li/a").click()
    #print('금산고등학교 클릭')
    #학교선택
    driver.find_element_by_xpath('//*[@id="softBoardListLayer"]/div[2]/div[2]/input').click()
    #print('학교 클릭')
    #성명 입력
    driver.find_element_by_xpath('//*[@id="user_name_input"]').send_keys('심화섭')
    #print('심화섭 입력')
    #생년월일 입력
    driver.find_element_by_xpath('//*[@id="birthday_input"]').send_keys('040331')
    #print('생년월일 입력')
    #확인 없어졌나봄
    #driver.find_element_by_xpath('//*[@id="btnConfirm"]').click()
    #여기도 가끔 오류남
    time.sleep(1)
    # driver.implicitly_wait(10) ## 암묵적으로 웹 자원을 (최대) 10초 기다리기 # 이거 아닌가봄
    #보안 키패드 클릭
    driver.find_element_by_xpath('//*[@id="WriteInfoForm"]/table/tbody/tr[4]/td/div/button').click()
    #print('보안 키패드 클릭')
    #여기는 체크하지 않음
    time.sleep(1)
    userpassword('1','2','3','4')
    #print('비밀번호 클릭 완료')
    #비밀번호 확인
    driver.find_element_by_xpath('//*[@id="btnConfirm"]').click()
    #print('비밀번호 확인')
    #오류로 인한 일시정지
    time.sleep(2)
    #계정 선택 (미참여 인거)
    driver.find_element_by_xpath('//*[@id="container"]/div/section[2]/div[2]/ul/li/a[1]').click()
    #print('미참여 클릭')
    #문제생김 일시정지
    time.sleep(1)
    # 1. 임상증상 아니요
    driver.find_element_by_xpath('//*[@id="survey_q1a1"]').click()
    #print('1. 임상증상 아니요')
    # 2. 신속항원검사 검사하지 않음
    driver.find_element_by_xpath('//*[@id="survey_q2a3"]').click()
    #print('2. 신속항원검사 검사하지 않음')
    # 2-1. 신속항원검사 음성 (월,수)
    #driver.find_element_by_xpath('//*[@id="survey_q2a1"]').click()
    # 3. 본인 또는 동거인 PCR검사결과 기다리고 있니요? 아니요
    driver.find_element_by_xpath('//*[@id="survey_q3a1"]').click()
    #print('3. 본인 또는 동거인 PCR검사결과 기다리고 있니요? 아니요')
    #제출
    driver.find_element_by_xpath('//*[@id="btnConfirm"]').click()
    #print('제출 완료')
    time.sleep(3)
    print(datetime.now())
    #브라우저 종료
    driver.quit()
    #print('브라우저 종료')