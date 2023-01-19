import json
from course.models import Course, Stacks, Course_Stacks, Company, Related_Stacks,Company_Stacks


# 제이슨 파일로 저장
def toJson(res_dict,save_name):
    with open(f'{save_name}.json', 'w', encoding='utf-8') as file :
        json.dump(res_dict, file, ensure_ascii=False, indent='\t')

# Course data
f = open(f'json/inflearn.json', encoding='UTF-8')
data = json.loads(f.read())  
# stack data
f = open(f'json/스택별.json', encoding='UTF-8')
data2 = json.loads(f.read()) 
# company data
f = open(f'json/stackDict.json', encoding='UTF-8')
data3 = json.loads(f.read()) 

# (사전 업데이트 시에만 필요)사전 리스트에 원래 스택 이름 없다면 추가해서 저장
# for i in data3:
#   if i not in data3[i]:
#     data3[i].append(i)
# toJson(data3,"stackDict")

# 기술 스택 이름 통일
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


# 강의 타이틀이나 헤드라인에 기술 사전에 해당하는 기술이 있다면 강의 기술 스택리스트에 추가("R"과 "Go"는 제외)
def run():
  # for i in data:
  #   new_stack = data[i]['stacks']
  #   for k,v in data3.items():
  #     if k not in ["Go","R","Java","Spring","Flow","Gin","Realm","Netty","Notion"]:
  #       for stack in v:
  #         if stack.lower() in i.lower() or stack.lower() in data[i]['headline'].lower():
  #           if k not in data[i]['stacks']:
  #             new_stack.append(k)
  #             print(i, data[i]['stacks'])
  #   data[i]['stacks'] = new_stack
    for i in data3:
      print(i)

  # toJson(data,"result")