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
    courseTime = models.CharField(max_length=50,default='')
    studentCnt = models.IntegerField(default=0, null=True)
    recommend = models.IntegerField(default=0,null=True)
    reviewCnt = models.IntegerField(default=0,null=True)
    price = models.IntegerField(default='',null=True)
    rank = models.FloatField(default=None, null=True)
    stack = models.ManyToManyField("Stacks",through='Course_Stacks')

    class Meta:
        db_table='Course'

# 스택테이블
class Stacks(models.Model):  
    name = models.CharField(max_length=30,unique=True)
    logo = models.URLField(max_length=100, default='')
    assort = models.URLField(max_length=15,default='')
    described = models.TextField()

    class Meta:
        db_table ='Stacks'

# Course_Stack 중간테이블
class Course_Stacks(models.Model):
    course =models.ForeignKey('Course',on_delete=models.CASCADE)
    stacks =models.ForeignKey('Stacks',on_delete=models.CASCADE)

    class Meta:
        db_table='Course_Stacks'

# 회사테이블
class Company(models.Model):
    name = models.CharField(max_length=30,unique=True)
    logo = models.URLField(max_length=100,default='')
    stack_info = models.CharField(max_length=100,default='')
    stack = models.ManyToManyField("Stacks",through='Company_Stacks')

    class Meta:
        db_table = 'Company'

#Company_Stack 중간테이블
class Company_Stacks(models.Model):
    company =models.ForeignKey('Company',on_delete=models.CASCADE)
    stacks =models.ForeignKey('Stacks',on_delete=models.CASCADE)

    class Meta:
        db_table = 'Company_Stacks'


#related_stack 테이블
class Related_Stacks(models.Model):
    stack_name= models.ForeignKey('Stacks',on_delete=models.CASCADE)
    related_stacks = models.CharField(max_length=20)

    class Meta:
        db_table = 'Related_Stacks'

#stack_dict 테이블
class Stacks_Dict(models.Model):
    stack_name= models.ForeignKey('Stacks',on_delete=models.CASCADE)
    search_word= models.CharField(max_length=20)

    class Meta:
        db_table = 'Stacks_Dict'