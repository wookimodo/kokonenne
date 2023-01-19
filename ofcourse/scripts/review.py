import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotInteractableException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.action_chains import ActionChains
import json

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.implicitly_wait(10)
driver.set_window_size(600,600)
# ===================================================================================================================================================================
# 제이슨 파일로 저장
def toJson(res_dict,save_name):
    with open(f'{save_name}.json', 'w', encoding='utf-8') as file :
        json.dump(res_dict, file, ensure_ascii=False, indent='\t')
# ===================================================================================================================================================================

# 제목, 상세페이지, 이미지, 추천수, 설명, 난이도, 강의시간, 강사, 수강생수, 리뷰수, 가격, 기술스택리스트

# driver.get("https://www.inflearn.com/courses/it-programming?order=seq&page=1")

# temp_dict={}

# 리뷰 탭 가서 리뷰 긁어오기

# '더보기' 자동으로 누르기 함수
def more_main_page():
    more_css = "#reviews > div.cd-review__more > button"
    try:
      is_more = driver.find_element(By.CSS_SELECTOR, more_css).is_displayed()
    except Exception as e:
      is_more = False
    # true/ false

    while is_more:
        try:
            driver.find_element(
            By.CSS_SELECTOR,
            more_css
            ).send_keys(Keys.ENTER)
            time.sleep(2)
        except Exception as e:
            break


# more_main_page()
def run():


    page = 8


    reviewDict = {}
    driver.get(f"https://www.inflearn.com/courses/it-programming?order=seq&page={page}")
    for i in range(1,25):
      review_list = []
      driver.find_element(
        By.CSS_SELECTOR,
        f"#courses_section > div > div > div > main > div.courses_container > div > div:nth-child({i}) > div > a"
        ).send_keys(Keys.ENTER)

      more_main_page()
      title = driver.find_element(By.CSS_SELECTOR,'h1.cd-header__title').text.rstrip('\n대시보드')
      items = driver.find_elements(By.CSS_SELECTOR,'div.review-el__body')
      for item in items[:300]:
          try:
              review_list.append(item.text.strip())
          except Exception as e:
              continue
      print('title : ', title)
      print('---------------------------------------------------')
      print('review : ', review_list)
      print('---------------------------------------------------')
      reviewDict[title] = {'review' : review_list}
      driver.back()
    
    toJson(reviewDict,f'reviewData{page}')