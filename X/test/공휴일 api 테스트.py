'''
import time

#sh,sm = input("24시 기준 실행시간을 입력해주세요 : ").split()


#if int(sh) < int(time.strftime('%H', time.localtime(time.time()))):
#    (int(sh)-1-int(time.strftime('%H', time.localtime(time.time()))))*60**2



#print(int(sh)*60**2+int(sm)*60+(23-int(time.strftime('%H', time.localtime(time.time()))))*60**2+(59-int(time.strftime('%M', time.localtime(time.time()))))*60+(60-int(time.strftime('%S', time.localtime(time.time())))))



print(int(time.strftime('%Y', time.localtime(time.time()))))
print(int(time.strftime('%m', time.localtime(time.time()))))
print(int(time.strftime('%d', time.localtime(time.time()))))
print(int(time.strftime('%H', time.localtime(time.time()))))
print(int(time.strftime('%M', time.localtime(time.time()))))
print(int(time.strftime('%S', time.localtime(time.time()))))
#요일을 숫자로 표시, 일월화수목금토, 0~6
print(int(time.strftime('%w', time.localtime(time.time()))))

#시간 분을 따로 받음 

#현재시간으로부터 자정까지 남은 시간을 초로 환산
print((23-int(time.strftime('%H', time.localtime(time.time()))))*60**2+(59-int(time.strftime('%M', time.localtime(time.time()))))*60+(60-int(time.strftime('%S', time.localtime(time.time())))))

def totalcount(year : int ,month : int):
    url = "http://apis.data.go.kr/B090041/openapi/service/SpcdeInfoService/getRestDeInfo"
    api_key_utf8 = "ZwivLrudvl%2FhrxYMBlaZ6xvtJedAxNHKtdER0N6vGRidDZEeM4yup%2BqB2VH9S9%2BcAhUdBSxqULAmTX7ZvvLuoA%3D%3D"
    api_key_decode = parse.unquote(api_key_utf8)

    params = {
        "ServiceKey": api_key_decode,
        "solYear": 2022,
        "numOfRows": 100,
        "solMonth": month
    }

    response = requests.get(url, params=params)
    xml = BeautifulSoup(response.text, "lxml")

    return int(xml.find('totalcount').get_text())
    


'''

from cgitb import text
import requests
from urllib import parse
import pandas as pd
from bs4 import BeautifulSoup
from datetime import datetime

def getHoliday(year: int) -> pd.DataFrame:
    url = "http://apis.data.go.kr/B090041/openapi/service/SpcdeInfoService/getRestDeInfo"
    api_key_utf8 = "ZwivLrudvl%2FhrxYMBlaZ6xvtJedAxNHKtdER0N6vGRidDZEeM4yup%2BqB2VH9S9%2BcAhUdBSxqULAmTX7ZvvLuoA%3D%3D"
    api_key_decode = parse.unquote(api_key_utf8)

    params = {
        "ServiceKey": api_key_decode,
        "solYear": year,
        "numOfRows": 100,
        "solMonth": datetime.today().strftime('%m')
    }

    response = requests.get(url, params=params)
    xml = BeautifulSoup(response.text, "lxml")
    items = xml.find('items')
    item_list = []
    for item in items:
        item_dict = {
            "이름": item.find("datename").text.strip(),
            "날짜": item.find("locdate").text.strip()
        }
        item_list.append(item_dict)

    return pd.DataFrame(item_list,xml.find("totalCount"))

#print(getHoliday(2022))

def dayoff():
    
    if int(datetime.today().strftime('%w')) == 0:
        return True
        
    elif int(datetime.today().strftime('%w')) == 6:
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
        xml = BeautifulSoup(response.text, "lxml")
        items = xml.find('items')
        item_list = []
        for item in items:
            item_list.append(item.find("locdate").get_text())
    
        for item in item_list:
            if int(item) == int(datetime.today().strftime("%Y%m%d")):
                return True
    return False
        

print(dayoff())
print(datetime.today().strftime('%w'))

    

#q=[{"이름": 'i',"날짜": 't'}]
#print(pd.DataFrame(q))






'''
import requests
import datetime
from bs4 import BeautifulSoup

def print_whichday(year, month, day) :
    r = ['월요일', '화요일', '수요일', '목요일', '금요일', '토요일', '일요일']
    aday = datetime.date(year, month, day)
    bday = aday.weekday()
    return r[bday]

def get_request_query(url, operation, params, serviceKey):
    import urllib.parse as urlparse
    params = urlparse.urlencode(params)
    request_query = url + '/' + operation + '?' + params + '&' + 'serviceKey' + '=' + serviceKey
    return request_query

year = 2022
#일반 인증키(Encoding)
mykey = "WoMViKPOmQYKGqkJxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

for month in range(1,13):

    if month < 10:
        month = '0' + str(month)
    else:
        month = str(month)
    
    url = 'http://apis.data.go.kr/B090041/openapi/service/SpcdeInfoService'
	#공휴일 정보 조회
    operation = 'getRestDeInfo'
    params = {'solYear':year, 'solMonth':month}

    request_query = get_request_query(url, operation, params, mykey)
    get_data = requests.get(request_query)    

    if True == get_data.ok:
        soup = BeautifulSoup(get_data.content, 'html.parser')        
        
        item = soup.findAll('item')
        #print(item);
        for i in item:
            
            day = int(i.locdate.string[-2:])
            weekname = print_whichday(int(year), int(month), day)
            print(i.datename.string, i.isholiday.string, i.locdate.string, weekname)
'''