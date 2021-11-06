from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import pyautogui as pagx
import pyautogui
import time
import time as t

#변수 설정

# 전국 구 시 리스트 형태로 제작
list_City =[
    '서울특별시','부산광역시','대구광역시','인천광역시','광주광역시','대전광역시','울산광역시','세종특별자치시',
    '경기도','강원도','충청북도','충청남도','전라북도','전라남도','경상북도','경상남도','제주특별자치도']
School_level_list = ['유치원','초등학교','중학교','고등학교','특수학교 등']
Numberlist=['1','2','3','4','5','6','7','8','9','0']
#생년월일
DateofBirth="050915"
#니 이름
name="임시온"#input("Your name: ")
#자가진단 비밀번호
pwd=input("Your password: ")
#학교 레벨
level = "고등학교"#input("Your school level")
#학교 이름
school="부산소프트웨어마이스터고등학교"#input("Your School name: ")
#거주하고 있는 도시
YCity="부산광역시"#input("The name of the city you live in?:")

driver = webdriver.Chrome('C:\\Users\\SW2126\\Desktop\\Python\\projects\\Macro_programs\\Auto_git\\chromedriver_win32\\chromedriver.exe')
url = 'https://google.com/'

#google connect function=====================================================
def start():
    driver.get(url)
    driver.maximize_window()

    #google search box find
    google_search_box = driver.find_element_by_css_selector('.gLFyf.gsfi')

    #driver send_keys
    google_search_box.send_keys('자가진단')
    google_search_box.send_keys(Keys.ENTER)
    
#=============================================================================

#=========시/도 선택하게 해주는 함수 =========================================
#can only concatenate str (not "int") to str 라는 거 떠서 str해줌
def Login_City():
    login_index = str(list_City.index(YCity)+2)
    driver.find_element_by_xpath(
    '//*[@id="sidolabel"]/option['+login_index+']'
         ).click()
#=============================================================================
def School_level():
    school_level_index = str(School_level_list.index(level)+2)
    driver.find_element_by_xpath(
    '//*[@id="crseScCode"]/option['+school_level_index+']'
    ).click()
#=============================================================================
def School_name():
    seracArea = driver.find_element_by_css_selector('.searchArea')
    seracArea.send_keys(school)
    seracArea.send_keys(Keys.TAB,Keys.ENTER)
    driver.find_element_by_xpath(
        '/html/body/div/div/div/div/div/div[2]/div[1]/table/tbody/tr[3]/td[2]/button'
    ).send_keys(Keys.TAB, Keys.ENTER)
    driver.find_element_by_css_selector('.layerFullBtn').click()
#=============================================================================
def named():
    namelink=driver.find_element_by_css_selector('#user_name_input')
    namelink.click()
    namelink.send_keys(name)
#============================================================================
def Date():
    Datelink=driver.find_element_by_css_selector('#birthday_input')
    Datelink.click()
    Datelink.send_keys(DateofBirth)
    driver.find_element_by_css_selector('#btnConfirm').click()
#============================================================================
def schools():
    Login_City()
    School_level()
    School_name()
#============================================================================
def password_click():
    driver.find_element_by_css_selector('#password').click()
    for p in pwd:
        time.sleep(0.2)
        img = pyautogui.locateCenterOnScreen('./NumberPictures/'+str(p)+'.PNG')
        pyautogui.click('./NumberPictures/'+str(p)+'.PNG')
    return
#=============================================================================
def last_click():
    time.sleep(2)
    driver.find_element_by_css_selector(
        '.service01').send_keys(Keys.TAB * 3, Keys.ENTER)
    time.sleep(2)
    driver.find_element_by_id("survey_q1a1").click()
    driver.find_element_by_id("survey_q2a1").click()
    driver.find_element_by_id("survey_q3a1").click()
    driver.find_element_by_id("btnConfirm").click()
#자가진단 사이트 들어가서 로그인 까지=========================================
def login_slef_Diagnosis():
    #자가진단 사이트 들어가기
    driver.find_element_by_css_selector('.LC20lb.DKV0Md').click()
    time.sleep(1)
    driver.find_element_by_css_selector('#btnConfirm2').click()
    time.sleep(1)
    driver.find_element_by_css_selector('#schul_name_input').click()
    time.sleep(1)
    schools()
    time.sleep(0.4)
    named()
    Date()
    t.sleep(1)
    password_click()
    driver.find_element_by_css_selector('#btnConfirm').click()
    last_click()
    print("finish!")

start()
login_slef_Diagnosis()