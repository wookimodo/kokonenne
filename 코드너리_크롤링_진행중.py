from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.keys import Keys
import json

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.implicitly_wait(10) 

# ===================================================================================================================================================================
# 제이슨 파일로 저장하는 함수
def toJson(temp_dict,save_name):
    with open(f'{save_name}.json', 'w', encoding='utf-8') as file :
        json.dump(temp_dict, file, ensure_ascii=False, indent='\t')
        
# ===================================================================================================================================================================
# dict
stack_dict = {}
temp_dict = {}

# ===================================================================================================================================================================
for j in range(1):
    # 최초 접속 URL 설정
    driver.get(f"https://www.codenary.co.kr/techstack/list?page={j+1}")

    for i in range(4): 
        try:
            # 기술명
            try:
                skill = driver.find_element(By.XPATH,f'//*[@id="root"]/div/section/div[2]/div/section/main/div[2]/nav/div/div[{i+1}]/figure/div/a/h4/span[2]/span[1]').text.strip()
            except Exception as e:
                skill = '-'

            # 로고 이미지
            try:
                logo = driver.find_element(By.XPATH,f'//*[@id="root"]/div/section/div[2]/div/section/main/div[2]/nav/div/div[{i+1}]/figure/div/a/h4/span[1]/img').get_attribute('src').strip()
            except Exception as e:
                logo = '-'

            # 상세 클릭 // 무슨짓을 해도 클릭이 안된다 싶을 땐 이렇게 하자
            element = driver.find_element(By.XPATH,f'//*[@id="root"]/div/section/div[2]/div/section/main/div[2]/nav/div/div[{i+1}]/figure/div/a')
            driver.execute_script("arguments[0].click();", element)
            time.sleep(2)
            print(f"{j+1}페이지 {i+1}번째")

            
            # 내용 긁어오기
            # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            # 1번 스택
            stack1_list = []
            try:                                                 
                stack1_main_name = driver.find_element(By.XPATH,'//*[@id="root"]/div/section/div[2]/div/section/main/div[2]/div/div[2]/div[1]/div[1]/div/div[1]/div/h1').text.strip()
                for li in range(15):
                    try:
                        try:                                        
                            # 언어 이름
                            stack1_name = driver.find_elements(By.XPATH,f'//*[@id="root"]/div/section/div[2]/div/section/main/div[2]/div/div[2]/div[1]/div[2]/div/div[{li+1}]/span[2]')[0].text.strip()
                            # 언어 이미지                           
                            stack1_img = driver.find_elements(By.XPATH,f'//*[@id="root"]/div/section/div[2]/div/section/main/div[2]/div/div[2]/div[1]/div[2]/div/div[{li+1}]/span[1]/img')[0].get_attribute('src').strip()
                            stack1_list.append([stack1_name,stack1_img]) # 빈 리스트에 하나씩 묶어서 넣기
                        except Exception as e:
                            break 
                    except Exception as e:
                        stack1_list = []
            except Exception as e:
                stack1_main_name = "1번 카테고리"
                stack1_list = None

            stack_dict = {
                stack1_main_name : stack1_list,
                # stack2_main_name : stack2_list,
                # stack3_main_name : stack3_list,
                # stack4_main_name : stack4_list,
                # stack5_main_name : stack5_list,
                # stack6_main_name : stack6_list,
                # stack7_main_name : stack7_list,
                # stack8_main_name : stack8_list,
                # stack9_main_name : stack9_list,
            }

            temp_dict[skill] = {
                'logo': logo,
                # 'stack_info' : stack_info, 
                'stacks' : stack_dict
            }

        except Exception as e:
            break
                        
    print("xx"*60)
    driver.back()
    toJson(temp_dict, "스킬정보")
time.sleep(1)
# ===================================================================================================================================================================
# 제이슨 파일로 저장
print("json 저장 완료")
driver.close()