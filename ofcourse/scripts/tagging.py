import json
from course.models import Course, Stack, Course_Stack, Company, Related_Stack,Company_Stack


# 제이슨 파일로 저장
def toJson(res_dict,save_name):
    with open(f'{save_name}.json', 'w', encoding='utf-8') as file :
        json.dump(res_dict, file, ensure_ascii=False, indent='\t')

# inflearn data
f = open(f'json/inflearn.json', encoding='UTF-8')
inflearn = json.loads(f.read())  
# stack data
f = open(f'json/스택별.json', encoding='UTF-8')
codenary = json.loads(f.read()) 
# company data
f = open(f'json/stackDict.json', encoding='UTF-8')
stackDict = json.loads(f.read()) 
# udemy data
f = open(f'json/udemy.json', encoding='UTF-8')
udemy = json.loads(f.read()) 
# allcourse data
f = open(f'json/udemy.json', encoding='UTF-8')
allcourse = json.loads(f.read()) 
# goorm data
f = open(f'json/goorm.json', encoding='UTF-8')
goorm = json.loads(f.read()) 
# allcourse data
f = open(f'json/allcourse.json', encoding='UTF-8')
allcourse = json.loads(f.read()) 

# goorm_sentiment data
f = open(f'json/goorm_sentiment.json', encoding='UTF-8')
goorm_sentiment = json.loads(f.read()) 

# goorm_sentiment data
f = open(f'json/inflearn_sentiment.json', encoding='UTF-8')
inflearn_sentiment = json.loads(f.read()) 


# 기술 스택 이름 통일(인프런)
# def run():
#   for i in data:
#     if "JavaScript" in data[i]['stacks']:
#       stacks = data[i]['stacks']
#       stacks.remove("JavaScript")
#       data[i]['stacks'] = stacks
      # if ".js" in stack:
      #   data[i]['stacks'].append(stack.replace(".js","JS"))
      #   print(stack)
  # toJson(data,"tmp")

# 강의 데이터 합치기(중복 강의 제거)
def run():
  for i in allcourse:
    allcourse[i] = allcourse[i]

  toJson(allcourse,"allcourse")



# 강의 타이틀이나 헤드라인에 기술 사전에 해당하는 기술이 있다면 강의 기술 스택리스트에 추가("R"과 "Go"는 제외)
# def run():
  # for i in udemy:
  #   new_stack = udemy[i]['stacks']
  #   for k,v in stackDict.items():
  #     if k not in ["Go","R","Java","Spring","Flow","Gin","Realm","Netty","Notion"]:
  #       for stack in v:
  #         if stack.lower() in i.lower() or stack.lower() in udemy[i]['headline'].lower():
  #           if k not in udemy[i]['stacks']:
  #             new_stack.append(k)
  #             print(i, udemy[i]['stacks'])
  #   udemy[i]['stacks'] = new_stack

  # for i in goorm:
  #   add_stack = goorm[i]['stacks']
  #   for k,v in stackDict.items():
  #     if k not in ["Go","R","Spring","Flow","Gin","Realm","Netty","Notion"]:
  #       for stack in v:
  #         if stack.lower() in i.lower() or stack.lower() in goorm[i]['headline'].lower():
  #           if k not in goorm[i]['stacks']:
  #             add_stack.append(k)
  #   goorm[i]['stacks'] = add_stack


  # toJson(goorm,"goorm")