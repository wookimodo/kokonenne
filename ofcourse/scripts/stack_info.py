import json

def toJson(res_dict,save_name):
    with open(f'{save_name}.json', 'w', encoding='utf-8') as file :
        json.dump(res_dict, file, ensure_ascii=False, indent='\t')

# 외국기업
# f = open(f'json/stackshare_all37개.json', encoding='UTF-8')
# foreign_company = json.loads(f.read())

# stack_info = "외국기업"

# for i in foreign_company:
#     foreign_company[i]['stack_info'] = stack_info

# toJson(foreign_company,"foreign_company.json")
# print("json 저장 완료")

# 국내기업
f = open(f'json/codenary.json', encoding='UTF-8')
domestic_company = json.loads(f.read())

stack_info = "국내기업"

for i in domestic_company:
    domestic_company[i]['stack_info'] = stack_info

toJson(domestic_company,"domestic_company")
print("json 저장 완료")