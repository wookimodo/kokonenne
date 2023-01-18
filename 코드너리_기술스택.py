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
# ===================================================================================================================================================================

# ===================================================================================================================================================================
# 최초 접속 URL 설정
stack_dict = {}
temp_dict = {}
# cnt = 0
# 사이트 로그인
# driver.get(f"https://www.codenary.co.kr/login")

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# 네이버로 로그인 클릭
# naver_id = 'hbt24'
# naver_pw = 'kong123'

# element = driver.find_element(By.XPATH,f'//*[@id="root"]/div/section/div[2]/div/section/main/div[2]/div/div/div/div/div/ul/li[1]/div') 
# driver.execute_script("arguments[0].click();", element)
# time.sleep(1)

# # 아이디 입력
# driver.find_element(By.XPATH,"//*[@id='id']").send_keys(naver_id)
# time.sleep(3)
# # 비밃번호 입력
# driver.find_element(By.XPATH,"//*[@id='pw']").send_keys(naver_pw)
# time.sleep(3)

# # 로그인 클릭
# driver.find_element(By.XPATH,"//*[@id='log.login']").click()
# driver.find_element(By.XPATH,"//*[@id='pw']").send_keys(naver_pw)

# time.sleep(20)

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

for j in range(14):
    driver.get(f"https://www.codenary.co.kr/company/list?page={j+1}")
    for i in range(12): 
        try:
            # 클릭 하기 전에 n개의 언어 어쩌고 긁기
            try:
                stack_info = driver.find_element(By.XPATH,f'//*[@id="root"]/div/section/div[2]/div/section/main/div[2]/nav/div/div[{i+1}]/div/div/a/div/div/div[3]/p').text.strip()
            except Exception as e:
                stack_info = '정보 없음'

            # 기업명
            try:
                company = driver.find_element(By.XPATH,f'//*[@id="root"]/div/section/div[2]/div/section/main/div[2]/nav/div/div[{i+1}]/div/div/a/div/div/div[1]/div[2]/div[1]/span').text.strip()
            except Exception as e:
                company = '정보 없음'

            # 로고 이미지
            try:
                logo = driver.find_element(By.XPATH,f'//*[@id="root"]/div/section/div[2]/div/section/main/div[2]/nav/div/div[{i+1}]/div/div/a/div/div/div[1]/div[1]/img').get_attribute('src').strip()
            except Exception as e:
                logo = '정보 없음'

            # 상세 클릭 // 무슨짓을 해도 클릭이 안된다 싶을 땐 이렇게 하자
            element = driver.find_element(By.XPATH,f'//*[@id="root"]/div/section/div[2]/div/section/main/div[2]/nav/div/div[{i+1}]/div/div/a/div/div')
            driver.execute_script("arguments[0].click();", element)
            time.sleep(2)
            print(i)

    # 내용 긁어오기
    # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            # 1번 스택
            stack1_list = []
            try:                                                 
                stack1_main_name = driver.find_element(By.XPATH,'//*[@id="root"]/div/section/div[2]/div/section/main/div[2]/div/div[2]/div[1]/div[1]/div/div[1]/div/h1').text.strip()
                for li in range(15):
                    try:
                        try:                                        
                            stack1_name = driver.find_elements(By.XPATH,f'//*[@id="root"]/div/section/div[2]/div/section/main/div[2]/div/div[2]/div[1]/div[2]/div/div[{li+1}]/span[2]')[0].text.strip()
                            # 언어 이름
                            stack1_img = driver.find_elements(By.XPATH,f'//*[@id="root"]/div/section/div[2]/div/section/main/div[2]/div/div[2]/div[1]/div[2]/div/div[{li+1}]/span[1]/img')[0].get_attribute('src').strip()
                            # 언어 이미지                           
                            stack1_list.append([stack1_name,stack1_img]) # 빈 리스트에 하나씩 묶어서 넣기
                        except Exception as e:
                            break 
                    except Exception as e:
                        stack1_list = []
            except Exception as e:
                stack1_main_name = "1번 카테고리"
                stack1_list = None

            # 2번 스택
            stack2_list = []
            try:
                stack2_main_name = driver.find_element(By.XPATH,'//*[@id="root"]/div/section/div[2]/div/section/main/div[2]/div/div[2]/div[2]/div[1]/div/div[1]/div/h1').text.strip()
                for li in range(15):
                    try:
                        try:
                            stack2_name = driver.find_elements(By.XPATH,f'//*[@id="root"]/div/section/div[2]/div/section/main/div[2]/div/div[2]/div[2]/div[2]/div/div[{li+1}]/span[2]')[0].text.strip()
                            # 언어 이름
                            stack2_img = driver.find_elements(By.XPATH,f'//*[@id="root"]/div/section/div[2]/div/section/main/div[2]/div/div[2]/div[2]/div[2]/div/div[{li+1}]/span[1]/img')[0].get_attribute('src').strip()
                            # 언어 이미지
                            stack2_list.append([stack2_name,stack2_img]) # 빈 리스트에 하나씩 묶어서 넣기
                        except Exception as e:
                            break 
                    except Exception as e:
                        stack2_list = []
            except Exception as e:
                stack2_main_name = "2번 카테고리"
                stack2_list = None

            # 3번 스택
            stack3_list = []
            try:
                stack3_main_name = driver.find_element(By.XPATH,'//*[@id="root"]/div/section/div[2]/div/section/main/div[2]/div/div[2]/div[3]/div[1]/div/div[1]/div/h1').text.strip()
                for li in range(15):
                    try:
                        try:
                            stack3_name = driver.find_elements(By.XPATH,f'//*[@id="root"]/div/section/div[2]/div/section/main/div[2]/div/div[2]/div[3]/div[2]/div/div[{li+1}]/span[2]')[0].text.strip()
                            # 언어 이름
                            stack3_img = driver.find_elements(By.XPATH,f'//*[@id="root"]/div/section/div[2]/div/section/main/div[2]/div/div[2]/div[3]/div[2]/div/div[{li+1}]/span[1]/img')[0].get_attribute('src').strip()
                            # 언어 이미지
                            stack3_list.append([stack3_name,stack3_img]) # 빈 리스트에 하나씩 묶어서 넣기
                        except Exception as e:
                            break 
                    except Exception as e:
                        stack3_list = []
            except Exception as e:
                stack3_main_name = "3번 카테고리"
                stack3_list = None

            # 4번 스택
            stack4_list = []
            try:
                stack4_main_name = driver.find_element(By.XPATH,'//*[@id="root"]/div/section/div[2]/div/section/main/div[2]/div/div[2]/div[4]/div[1]/div/div[1]/div/h1').text.strip()
                for li in range(15):
                    try:
                        try:
                            stack4_name = driver.find_elements(By.XPATH,f'//*[@id="root"]/div/section/div[2]/div/section/main/div[2]/div/div[2]/div[4]/div[2]/div/div[{li+1}]/span[2]')[0].text.strip()
                            # 언어 이름
                            stack4_img = driver.find_elements(By.XPATH,f'//*[@id="root"]/div/section/div[2]/div/section/main/div[2]/div/div[2]/div[4]/div[2]/div/div[{li+1}]/span[1]/img')[0].get_attribute('src').strip()
                            # 언어 이미지
                            stack4_list.append([stack4_name,stack4_img]) # 빈 리스트에 하나씩 묶어서 넣기
                        except Exception as e:
                            break 
                    except Exception as e:
                        stack4_list = []
            except Exception as e:
                stack4_main_name = "4번 카테고리"
                stack4_list = None

            # 5번 스택
            stack5_list = []
            try:
                stack5_main_name = driver.find_element(By.XPATH,'//*[@id="root"]/div/section/div[2]/div/section/main/div[2]/div/div[2]/div[5]/div[1]/div/div[1]/div/h1').text.strip()
                for li in range(15):
                    try:
                        try:
                            stack5_name = driver.find_elements(By.XPATH,f'//*[@id="root"]/div/section/div[2]/div/section/main/div[2]/div/div[2]/div[5]/div[2]/div/div[{li+1}]/span[2]')[0].text.strip()
                            # 언어 이름
                            stack5_img = driver.find_elements(By.XPATH,f'//*[@id="root"]/div/section/div[2]/div/section/main/div[2]/div/div[2]/div[5]/div[2]/div/div[{li+1}]/span[1]/img')[0].get_attribute('src').strip()
                            # 언어 이미지
                            stack5_list.append([stack5_name,stack5_img]) # 빈 리스트에 하나씩 묶어서 넣기
                        except Exception as e:
                            break 
                    except Exception as e:
                        stack5_list = []
            except Exception as e:
                stack5_main_name = "5번 카테고리"
                stack5_list = None

            # 6번 스택
            stack6_list = []
            try:
                stack6_main_name = driver.find_element(By.XPATH,'//*[@id="root"]/div/section/div[2]/div/section/main/div[2]/div/div[2]/div[6]/div[1]/div/div[1]/div/h1').text.strip()
                for li in range(15):
                    try:
                        try:
                            stack6_name = driver.find_elements(By.XPATH,f'//*[@id="root"]/div/section/div[2]/div/section/main/div[2]/div/div[2]/div[6]/div[2]/div/div[{li+1}]/span[2]')[0].text.strip()
                            # 언어 이름
                            stack6_img = driver.find_elements(By.XPATH,f'//*[@id="root"]/div/section/div[2]/div/section/main/div[2]/div/div[2]/div[6]/div[2]/div/div[{li+1}]/span[1]/img')[0].get_attribute('src').strip()
                            # 언어 이미지
                            stack6_list.append([stack6_name,stack6_img]) # 빈 리스트에 하나씩 묶어서 넣기
                        except Exception as e:
                            break 
                    except Exception as e:
                        stack6_list = []
            except Exception as e:
                stack6_main_name = "6번 카테고리"
                stack6_list = None

            # 7번 스택
            stack7_list = []
            try:
                stack7_main_name = driver.find_element(By.XPATH,'//*[@id="root"]/div/section/div[2]/div/section/main/div[2]/div/div[2]/div[7]/div[1]/div/div[1]/div/h1').text.strip()
                for li in range(15):
                    try:
                        try:
                            stack7_name = driver.find_elements(By.XPATH,f'//*[@id="root"]/div/section/div[2]/div/section/main/div[2]/div/div[2]/div[7]/div[2]/div/div[{li+1}]/span[2]')[0].text.strip()
                            # 언어 이름
                            stack7_img = driver.find_elements(By.XPATH,f'//*[@id="root"]/div/section/div[2]/div/section/main/div[2]/div/div[2]/div[7]/div[2]/div/div[{li+1}]/span[1]/img')[0].get_attribute('src').strip()
                            # 언어 이미지
                            stack7_list.append([stack7_name,stack7_img]) # 빈 리스트에 하나씩 묶어서 넣기
                        except Exception as e:
                            break 
                    except Exception as e:
                        stack7_list = []
            except Exception as e:
                stack7_main_name = "7번 카테고리"
                stack7_list = None

            # 8번 스택
            stack8_list = []
            try:
                stack8_main_name = driver.find_element(By.XPATH,'//*[@id="root"]/div/section/div[2]/div/section/main/div[2]/div/div[2]/div[8]/div[1]/div/div[1]/div/h1').text.strip()
                for li in range(15):
                    try:
                        try:
                            stack8_name = driver.find_elements(By.XPATH,f'//*[@id="root"]/div/section/div[2]/div/section/main/div[2]/div/div[2]/div[8]/div[2]/div/div[{li+1}]/span[2]')[0].text.strip()
                            # 언어 이름
                            stack8_img = driver.find_elements(By.XPATH,f'//*[@id="root"]/div/section/div[2]/div/section/main/div[2]/div/div[2]/div[8]/div[2]/div/div[{li+1}]/span[1]/img')[0].get_attribute('src').strip()
                            # 언어 이미지
                            stack8_list.append([stack8_name,stack8_img]) # 빈 리스트에 하나씩 묶어서 넣기
                        except Exception as e:
                            break 
                    except Exception as e:
                        stack8_list = []
            except Exception as e:
                stack8_main_name = "8번 카테고리"
                stack8_list = None

            # 9번 스택
            stack9_list = []
            try:
                stack9_main_name = driver.find_element(By.XPATH,'//*[@id="root"]/div/section/div[2]/div/section/main/div[2]/div/div[2]/div[9]/div[1]/div/div[1]/div/h1').text.strip()
                for li in range(15):
                    try:
                        try:
                            stack9_name = driver.find_elements(By.XPATH,f'//*[@id="root"]/div/section/div[2]/div/section/main/div[2]/div/div[2]/div[9]/div[2]/div/div[{li+1}]/span[2]')[0].text.strip()
                            # 언어 이름
                            stack9_img = driver.find_elements(By.XPATH,f'//*[@id="root"]/div/section/div[2]/div/section/main/div[2]/div/div[2]/div[9]/div[2]/div/div[{li+1}]/span[1]/img')[0].get_attribute('src').strip()
                            # 언어 이미지
                            stack9_list.append([stack9_name,stack9_img]) # 빈 리스트에 하나씩 묶어서 넣기
                        except Exception as e:
                            break 
                    except Exception as e:
                        stack9_list = []
            except Exception as e:
                stack9_main_name = "9번 카테고리"
                stack9_list = None

            stack_dict = {
                stack1_main_name : stack1_list,
                stack2_main_name : stack2_list,
                stack3_main_name : stack3_list,
                stack4_main_name : stack4_list,
                stack5_main_name : stack5_list,
                stack6_main_name : stack6_list,
                stack7_main_name : stack7_list,
                stack8_main_name : stack8_list,
                stack9_main_name : stack9_list,
            }

            temp_dict[company] = {
                'logo': logo,
                'stack_info' : stack_info, 
                'stacks' : stack_dict
            }

        except Exception as e:
            break
                        
        print("xx"*60)
        driver.back()
        toJson(temp_dict,"테스트")
    # print(temp_dict)
    time.sleep(1)
# ===================================================================================================================================================================
# 제이슨 파일로 저장
print("json 저장 완료")
driver.close()