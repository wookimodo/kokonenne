from django.shortcuts import render
from .models import Course, Stacks, Course_Stacks
from django.views.generic import ListView, FormView,View
from .forms import CourseSearchForm
from django.db.models import Q
from django.core.paginator import Paginator

# def list(requests):
#     # db에서 data query해서 오기
#     course = Course.objects.all()
#     stacks = Stacks.objects.all()
#     return render(requests, 'course/list.html', {"course":course, "stacks":stacks})

# Create your views here.

class Courselist(ListView):
    model = Course
    template_name ='course/list.html'

    def get_context_data(self, **kwargs):
        context = super(Courselist, self).get_context_data()
        context['stacks'] = Stacks.objects.all()
        return context

# search FBV형2
def search(request):
    paginate_by = 15
    stacks = []
    course_list = Course.objects.all()
    stack_list = Stacks.objects.all()
    search = request.GET.get('search','')
    s = request.GET.getlist('s')
    level = request.GET.get('level','')

    if search:
        search_list = course_list.filter(
            Q(title__icontains=search) |
            Q(teacher__icontains=search) |
            Q(headline__icontains=search) |
            Q(stack__name__icontains=search)
        ).distinct()
    if s: # 체크박스에서 값이 넘어오면
        for i in s:
            course_list = course_list.filter(
                Q(stack__name__icontains=i))
            stacks.append(stack_list.get(
                Q(name__iexact=i)
            ))
    # context['is_paginated'] = True

    # paginator = Paginator(course_list,paginate_by)
    # page_number_range = 10
    # current_page = int(request.GET.get('page,1'))
    # context['current_page'] = current_page

    # # 시작/끝 index 조회
    # start_index = int((current_page-1)/page_number_range)*page_number_range
    # end_index = start_index + page_number_range

    # # 현재 페이지가 속한 페이지 그룹의 범위
    # current_page_group_range = paginator.page_range[start_index:end_index]

    # start_page = paginator.page(current_page_group_range[0])
    # end_page = paginator.page(current_page_group_range[-1])







    # paginator = Paginator(search_list, 10)
    # page = request.GET.get('page', '')
    # course = paginator.get_page(page)

    return render(request, 'course/course_search.html',{'course':course_list, 'search':search,'stacks':stacks})