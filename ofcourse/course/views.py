from django.shortcuts import render
from .models import Course, Stack, Course_Stack
from django.views.generic import ListView, FormView,View
from .forms import CourseSearchForm
from django.db.models import Q
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    stack_list = Stack.objects.all()
    return render(request, 'index.html', {'stack_list': stack_list})

class Courselist(ListView):
    model = Course
    paginate_by = 300
    template_name ='course/list.html'
    ordering ='rank'

    # ListView를 사용할땐 get_context_data를 안해도 됨. 자동으로 해줌.
    def get_context_data(self, **kwargs):
        context = super(Courselist, self).get_context_data()
        context['stack'] = Stack.objects.all()
        return context

# search FBV형
def search(request):
    course_list = Course.objects.all().order_by('rank')
    search = request.GET.get('search','')
    if search:
        search_list = course_list.filter(
            Q(title__icontains=search) |
            Q(teacher__icontains=search) |
            Q(headline__icontains=search) |
            Q(stack__name__icontains=search) |
            Q(stack__stack_dict__search_word__icontains=search)
        ).distinct()
        # print(search_list.query)

        # print(search_list[5].title)
    paginator = Paginator(search_list, 10)
    page = request.GET.get('page', '')
    course = paginator.get_page(page)

    return render(request, 'course/course_search.html',{'course':course, 'search':search})

    # search FBV형2
def filter(request):
    course_list = Course.objects.all().order_by('rank')
    stack_list = Stack.objects.all()
    s = request.GET.getlist('s')

    if s: # 체크박스에서 값이 넘어오면
        course_query = Q()
        stack_query = Q()
        for i in s:
            # or 조건을 주기 위함
            course_query = course_query | Q(stack__name__iexact=i)
            stack_query = stack_query | Q(name__iexact=i)
        filter_list = course_list.filter(course_query)
        stack = stack_list.filter(stack_query)

    return render(request, 'course/course_filter.html',{'course':filter_list, 'stack':stack})
