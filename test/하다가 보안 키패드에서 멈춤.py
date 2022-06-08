from time import sleep
from selenium import webdriver
driver = webdriver.Chrome()
url = 'https://hcs.eduro.go.kr/#/loginHome'
driver.get(url)
driver.find_element_by_xpath('//*[@id="btnConfirm2"]').click()
driver.find_element_by_xpath('//*[@id="schul_name_input"]').click()
driver.find_element_by_xpath('//*[@id="sidolabel"]/option[13]').click()
driver.find_element_by_xpath('//*[@id="crseScCode"]/option[5]').click()
driver.find_element_by_xpath('//*[@id="orgname"]').send_keys('금산고등학교')
driver.find_element_by_xpath('//*[@id="softBoardListLayer"]/div[2]/div[1]/table/tbody/tr[3]/td[2]/button').click()
#driver.find_element_by_xpath('//*[@id="softBoardListLayer"]/div[2]/div[1]/ul').click()
sleep(0.1)
driver.find_element_by_xpath("//*[@id='softBoardListLayer']/div[2]/div[1]/ul/li/a").click() #.send_keys(Keys.ENTER)
driver.find_element_by_xpath('//*[@id="softBoardListLayer"]/div[2]/div[2]/input').click()
driver.find_element_by_xpath('//*[@id="user_name_input"]').send_keys('심화섭')
driver.find_element_by_xpath('//*[@id="birthday_input"]').send_keys('040331')
driver.find_element_by_xpath('//*[@id="btnConfirm"]').click()
sleep(1)
driver.find_element_by_xpath('//*[@id="WriteInfoForm"]/table/tbody/tr/td/div/button').click()

driver.find_element_by_xpath('//div/a[aria-label="5"]').click()
#driver.find_element_by_xpath('//*[@id="WriteInfoForm"]/table/tbody/tr/td/div/button').click()
#driver.find_element_by_xpath('//*[@id="WriteInfoForm"]/table/tbody/tr/td/div/button').click()
#driver.find_element_by_xpath('//*[@id="WriteInfoForm"]/table/tbody/tr/td/div/button').click()
#driver.find_element_by_xpath('//*[@id="WriteInfoForm"]/table/tbody/tr/td/div/button').click()




sleep(200)