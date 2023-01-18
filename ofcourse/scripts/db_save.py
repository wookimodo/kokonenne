import json
# import os
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ofcourse.settings")
# import django
# django.setup()
from course.models import Course, Stacks, Course_Stacks, Company, Related_Stacks,Company_Stacks

# Course data
f = open(f'json/inflearn.json', encoding='UTF-8')
data = json.loads(f.read())  
# stack data
f = open(f'json/스택별.json', encoding='UTF-8')
data2 = json.loads(f.read()) 
# company data
f = open(f'json/회사별.json', encoding='UTF-8')
data3 = json.loads(f.read()) 

# 제이슨 파일로 저장
def toJson(res_dict,save_name):
    with open(f'{save_name}.json', 'w', encoding='utf-8') as file :
        json.dump(res_dict, file, ensure_ascii=False, indent='\t')
    
# price 값 전처리 (,제거) - 완료됐음
# for i in data:
#     data[i]['price'] = data[i]['price'].replace(",","")

# Course 테이블 저장
def run():

    for i in data:
        url = data[i]['url']
        img_url = data[i]['image']
        title = i
        teacher = data[i]['teacher']
        headline = data[i]['headline']
        level = data[i]['level']
        score = data[i]['score']
        courseTime = data[i]['courseTime']
        studentCnt = data[i]['student']
        recommend = data[i]['recommend']
        reviewCnt = data[i]['reviewCnt']
        price = data[i]['price']
        rank = data[i]['rank']
        Course(
            url=url, 
            img_url=img_url, 
            title=title,
            teacher=teacher,
            headline=headline,
            level=level,
            score=score,
            courseTime=courseTime,
            studentCnt=studentCnt,
            recommend=recommend,
            reviewCnt=reviewCnt,
            price=price,
            rank=rank
        ).save()
    # Stacks테이블 저장
    # for i in data2:
    #     stack = i
    #     logo = data2[i]['logo']
    #     assort = data2[i]['assort']
    #     described = data2[i]['described']
        
    #     Stacks(
    #         name = stack,
    #         logo = logo,
    #         assort = assort,
    #         described = described            ```
    #     ).save()

    # Course_Stacks 중간테이블
    for i in data2:
        for j in data:
            if i in data[j]['stacks']:
                Course_Stacks(course_id=Course.objects.get(title=j).pk,stacks_id=Stacks.objects.get(name=i).pk).save()


    print('DB저장완료')