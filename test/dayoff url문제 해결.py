from html.parser import HTMLParser
import requests,time,csv
from urllib import parse
from datetime import datetime
from bs4 import BeautifulSoup
from selenium import webdriver
def dayoff():
    if int(datetime.today().strftime('%w')) == 0 or int(datetime.today().strftime('%w')) == 6:
        return True
    #elif int(datetime.today().strftime('%w')) == 6:
    #    return True
    else:
        #url = "http://apis.data.go.kr/B090041/openapi/service/SpcdeInfoService"
        url = "http://apis.data.go.kr/B090041/openapi/service/SpcdeInfoService/getRestDeInfo?ServiceKey=ZwivLrudvl%2FhrxYMBlaZ6xvtJedAxNHKtdER0N6vGRidDZEeM4yup%2BqB2VH9S9%2BcAhUdBSxqULAmTX7ZvvLuoA%3D%3D"+"&solYear="+str(datetime.today().year)+"&solMonth="+str(datetime.today().strftime('%m'))
        #api_key_utf8 = "ZwivLrudvl%2FhrxYMBlaZ6xvtJedAxNHKtdER0N6vGRidDZEeM4yup%2BqB2VH9S9%2BcAhUdBSxqULAmTX7ZvvLuoA%3D%3D"
        #api_key_decode = parse.unquote(api_key_utf8)
        #params = {
        #    "ServiceKey": api_key_utf8,#api_key_decode,
        #    "solYear": datetime.today().year,
        #    "numOfRows": 100,
        #    "solMonth": datetime.today().strftime('%m')
        #}
        #print(datetime.today().year, datetime.today().strftime('%m'))
        response = requests.get(url)#, params=params)
        xml = BeautifulSoup(response.text, 'html.parser')
        print(xml)
        items = xml.find('items')
        item_list = []
        for item in items:
            item_list.append(item.find("locdate").get_text())
    
        for item in item_list:
            if int(item) == int(datetime.today().strftime("%Y%m%d")):
                return True
    return False

print(dayoff())
    