import json
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ofcourse.settings")
from course.models import Course, Stacks
import django
django.setup()

f = open(f'inflearn test', encoding='UTF-8')
data = json.loads(f.read())

# Course 테이블 저장
for i in data:
    print(i)