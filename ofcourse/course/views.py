from django.shortcuts import render
from .models import Course, Stacks
# from django.views.generic import ListView

def list(requests):
    # db에서 data query해서 오기
    course = Course.objects.all()
    stacks = Stacks.objects.all()
    return render(requests, 'course/list.html', {"course":course, "stacks":stacks})

# Create your views here.
