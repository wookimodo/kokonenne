import json
# import os
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ofcourse.settings")
# import django
# django.setup()
from course.models import Course, Stack, Course_Stack, Company, Related_Stack,Company_Stack, Stack_Dict

# Course data
f = open(f'json/allcourse.json', encoding='UTF-8')
data = json.loads(f.read())  
# stack data
f = open(f'json/스택별.json', encoding='UTF-8')
data2 = json.loads(f.read()) 
# company data
f = open(f'json/codenary.json', encoding='UTF-8')
data3 = json.loads(f.read()) 

# stack_dict data
f = open(f'json/stackDict.json', encoding='UTF-8')
data4 = json.loads(f.read()) 

# 제이슨 파일로 저장
def toJson(res_dict,save_name):
    with open(f'{save_name}.json', 'w', encoding='utf-8') as file :
        json.dump(res_dict, file, ensure_ascii=False, indent='\t')
    

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
        student_cnt = data[i]['student']
        recommend = data[i]['recommend']
        review_cnt = data[i]['reviewCnt']
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
            student_cnt=student_cnt,
            recommend=recommend,
            review_cnt=review_cnt,
            price=price,
            rank=rank
        ).save()
    # Stack테이블 저장
    for i in data2:
        stack = i
        logo = data2[i]['logo']
        assort = data2[i]['assort']
        described = data2[i]['described']
        
        Stack(
            name = stack,
            logo = logo,
            assort = assort,
            described = described            
        ).save()

    # Course_Stack 중간테이블
    for i in data2:
        for j in data:
            if i in data[j]['stacks']:
                Course_Stack(course_id=Course.objects.get(title=j).pk,stack_id=Stack.objects.get(name=i).pk).save()

    # Company 테이블
    for i in data3:
        name = i
        logo = data3[i]['logo']
        stack_info = data3[i]['stack_info']

        Company(name=name, logo=logo, stack_info=stack_info).save()

    # Company_Stack 테이블
    for i in data3:
        for k,v in data3[i]['stacks'].items():
            if v != None:
                for stack in data3[i]['stacks'][k]:
                    Company_Stack(company_id=Company.objects.get(name=i).pk,stack_id=Stack.objects.get(name=stack[0]).pk).save()

    # related_stack 테이블
    for i in data2:
        stack_name_id = Stack.objects.get(name=i).pk
        for k in data2[i]['related_stacks']:
            related_stack_pk = Stack.objects.get(name=k).pk
            logo = Stack.objects.get(name=k).logo
            Related_Stack(stack_name_id=stack_name_id, related_stack=k, related_stack_logo=logo, related_stack_pk=related_stack_pk).save()

    # Stack_Dict테이블 
    for i in data2:
        stack_name_id = Stack.objects.get(name=i).pk
        for j in data4[i]:
            Stack_Dict(stack_name_id=stack_name_id, search_word=j).save()

    print('DB저장완료')
