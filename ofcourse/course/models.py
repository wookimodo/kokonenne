from django.db import models



# Create your models here.

# 강의 모델
class Course(models.Model):
    urlid = models.CharField(primary_key=True, default=None,max_length=100)
    url = models.URLField(max_length=100,default=None)
    img_url = models.URLField(max_length=250,default=None)
    title = models.CharField(max_length=30,default=None)
    teacher = models.CharField(max_length=30,default='')
    headline = models.TextField(default='')
    level = models.CharField(max_length=10,default='')
    score = models.FloatField(default=0, null=True)
    courseTime = models.CharField(max_length=50,default='')
    studentCnt = models.IntegerField(default=0,null=True)
    recommend = models.IntegerField(default=0,null=True)
    reviewCnt = models.IntegerField(default=0,null=True)
    price = models.IntegerField(default='',null=True)

# 기술스택 모델

class Stacks(models.Model):
    urlid = models.ForeignKey('Course',null=True,on_delete=models.SET_NULL)
    stacks = models.CharField(max_length=15, default='') 
