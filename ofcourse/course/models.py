from django.db import models
import uuid
# 여기


# Create your models here.

# 강의 모델
class Course(models.Model):
    urlid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    url = models.URLField(max_length=100,default=None)
    img_url = models.URLField(max_length=250,default=None)
    title = models.CharField(max_length=30,default=None)
    teacher = models.CharField(max_length=30,default='')
    headline = models.TextField(default='')
    level = models.CharField(max_length=10,default='')
    score = models.IntegerField(default=0)
    courseTime = models.CharField(max_length=50,default='')
    stduentCnt = models.IntegerField(default=0)
    recommend = models.IntegerField(default=0)
    reviewCnt = models.IntegerField(default=0)
    price = models.IntegerField(default='')

# 기술스택 모델

class Stacks(models.Model):
    urlid = models.ForeignKey('Course',null=True,on_delete=models.SET_NULL)
    stacks = models.CharField(max_length=15, default='')