from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import pyautogui as pagx
import pyautogui
import time
import time as t

#변수 설정
#니 이름
name=input("Your name: ")
#자가진단 비밀번호
pwd=input("Your password: ")
#학교 이름
school=input("Your School name: ")
#거주하고 있는 도시
YCity=input("The name of the city you live in?:")

driver = webdriver.Chrome('C:\\Users\\SW2126\\Desktop\\Python\\projects\\Macro_programs\\Auto_git\\chromedriver_win32\\chromedriver.exe')
url = 'https://google.com/'

driver.get(url)
driver.maximize_window()

#google search box find
google_search_box = driver.find_element_by_css_selector('.gLFyf.gsfi')

#driver send_keys
google_search_box.send_keys('자가진단')
google_search_box.send_keys(Keys.ENTER)
time.sleep(1)
driver.find_element_by_css_selector('.LC20lb.DKV0Md').click()
time.sleep(1)
driver.find_element_by_css_selector('#btnConfirm2').click()
time.sleep(1)
driver.find_element_by_css_selector('#schul_name_input').click()
time.sleep(1)
# 전국 구 시 리스트 형태로 제작
list_City =[
    '서울특별시','부산광역시','대구광역시','인천광역시','광주광역시','대전광역시','울산광역시','세종특별자치시',
    '경기도','강원도','충청북도','충청남도','전라북도','전라남도','경상북도','경상남도','제주특별자치도']
#print(real_City)
login_index = (list_City.index(YCity)+2)
driver.find_element_by_xpath(
    '//*[@id="sidolabel"]/option['+login_index+']'
).click()
