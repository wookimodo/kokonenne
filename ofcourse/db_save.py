import json
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ofcourse.settings")
import django
django.setup()
from course.models import Course, Stacks

f = open(f'modify.json', encoding='UTF-8')
data = json.loads(f.read())  

# Course 테이블 저장
# for i in data:
#     urlid = data[i]['pwdurl']
#     url = data[i]['url']
#     img_url = data[i]['image']
#     title = i
#     teacher = data[i]['teacher']
#     headline = data[i]['headline']
#     level = data[i]['level']
#     score = data[i]['score']
#     courseTime = data[i]['courseTime']
#     studentCnt = data[i]['student']
#     recommend = data[i]['recommend']
#     reviewCnt = data[i]['reviewCnt']
#     price = data[i]['price']
#     print(urlid)
#     try :
#         Course(urlid=urlid, 
#             url=url, 
#             img_url=img_url, 
#             title=title,
#             teacher=teacher,
#             headline=headline,
#             level=level,
#             score=score,
#             courseTime=courseTime,
#             studentCnt=studentCnt,
#             recommend=recommend,
#             reviewCnt=reviewCnt,
#             price=price
#         ).save()
#     except Exception as e:
#         print(e)


# Stacks테이블 저장
for i in data:
    urlid = data[i]['pwdurl']
    stack_lst = data[i]['stacks']
    for j in stack_lst:
        stack = j
    
        try:
            Stacks(urlid=Course.objects.get(pk=urlid), stacks=stack).save()
        except Exception as e:
            print(e)
print("DB저장완료")
#develop
