import json
from course.models import Course, Stacks
f = open(f'modify.json', encoding='UTF-8')
data = json.loads(f.read())
print(data)
def run():
    # Course 테이블 저장
    for i in data:
        urlid = data[i]['pwdurl']
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
        print(urlid)
        Course(urlid=urlid,
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
    for i in data:
        urlid = data[i]['pwdurl']
        stack_lst = data[i]['stacks']
        # if stack_lst == ["None"]:
        #     Stacks(urlid=Course.objects.get(pk=urlid), stacks=None).save()
        # else:
        for j in stack_lst:
            stack = j
            Stacks(urlid=Course.objects.get(pk=urlid), stacks=stack).save()
print("DB저장완료")
#develop