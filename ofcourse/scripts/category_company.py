import json
from course.models import Company

def toJson(res_dict,save_name):
    with open(f'{save_name}.json', 'w', encoding='utf-8') as file :
        json.dump(res_dict, file, ensure_ascii=False, indent='\t')

f = open(f'json/코드너리_스택별_최종.json', encoding='UTF-8')
category = json.loads(f.read())

f = open(f'json/codenary_re.json', encoding='UTF-8')
link = json.loads(f.read())

# 국내기업
f = open(f'json/최종 domestic_company.json', encoding='UTF-8')
company = json.loads(f.read())

# lst = []
# for i in category:
#     for k,v in category[i]['company_category'].items():
#         if v != None:
#             name=v[0][0]
#             if(Company.objects.filter(name__iexact=name)):
#                 lst.append((k,name))
# a = set(lst)
# a = sorted(a)

# for i in company:
#     for k,v in a:
#         if i != v:
#             print(i)
            # company[i]['category'] = k
# toJson(company,"최종 domestic_company")
# print("json 저장 완료")
        


for i in link:
    c_link = link[i]['company_link']
    r_link = link[i]['company_recruit_link']
    company[i]['company_link'] = c_link
    company[i]['company_recruit_link'] = r_link

toJson(company,"수정링크")
print("json 저장 완료")