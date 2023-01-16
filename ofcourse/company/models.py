from django.db import models
from django.shortcuts import render

# Create your models here.

class Company(models.Model):
    company = models.CharField(primary_key=True, max_length=10,default=None)
    logo = models.URLField(max_length=250,default=None)
    stack_info = models.CharField(max_length=30)

    


class CompanyDetail(models.Model):
    company = models.ForeignKey('Company', null=True,on_delete=models.SET_NULL, db_column='company')
    stack_name = models.CharField(max_length=100)
    stack_img = models.URLField(max_length=250)

    def get_absolute_url(self):  # company_detail 볼 때 
        return reverse("company:company_detail", kwargs={"pk": self.pk})



