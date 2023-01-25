from django.db import models

# Create your models here.

# 강의 모델
class Course(models.Model):
    url = models.URLField(max_length=100, default=None)
    img_url = models.URLField(max_length=250, default=None)
    title = models.CharField(max_length=30,default=None)
    teacher = models.CharField(max_length=30,default='')
    headline = models.TextField(default='')
    level = models.CharField(max_length=10,default='')
    score = models.FloatField(default=0, null=True)
    course_time = models.CharField(max_length=50,default='')
    student_cnt = models.IntegerField(default=0, null=True)
    recommend = models.IntegerField(default=0,null=True)
    review_cnt = models.IntegerField(default=0,null=True)
    price = models.IntegerField(default='',null=True)
    rank = models.FloatField(default=None, null=True)
    stack = models.ManyToManyField("Stack",through='Course_Stack')

    class Meta:
        db_table='Course'

# 스택테이블
class Stack(models.Model):  
    name = models.CharField(max_length=30,unique=True)
    logo = models.URLField(max_length=100, default='')
    assort = models.CharField(max_length=15,default='')
    described = models.TextField()

    class Meta:
        db_table ='Stack'

# Course_Stack 중간테이블
class Course_Stack(models.Model):
    course =models.ForeignKey('Course',on_delete=models.CASCADE)
    stack =models.ForeignKey('Stack',on_delete=models.CASCADE)

    class Meta:
        db_table='Course_Stack'

# 회사테이블
class Company(models.Model):
    name = models.CharField(max_length=30,unique=True)
    logo = models.URLField(max_length=100,default='')
    stack_info = models.CharField(max_length=100,default='')
    stack = models.ManyToManyField("Stack",through='Company_Stack')
    category = models.CharField(max_length=30,null=True)

    class Meta:
        db_table = 'Company'

#Company_Stack 중간테이블
class Company_Stack(models.Model):
    company =models.ForeignKey('Company',on_delete=models.CASCADE)
    stack =models.ForeignKey('Stack',on_delete=models.CASCADE)

    class Meta:
        db_table = 'Company_Stack'


#related_stack 테이블
class Related_Stack(models.Model):
    stack_name= models.ForeignKey('Stack',on_delete=models.CASCADE)
    related_stack = models.CharField(max_length=20)
    related_stack_logo = models.URLField(max_length=100,default='')
    related_stack_pk = models.IntegerField(default=0)

    class Meta:
        db_table = 'Related_Stack'

#stack_dict 테이블 입니다.
class Stack_Dict(models.Model):
    stack_name= models.ForeignKey('Stack',on_delete=models.CASCADE)
    search_word= models.CharField(max_length=20)

    class Meta:
        db_table = 'Stack_Dict'