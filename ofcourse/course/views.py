from django.shortcuts import render
from .models import Course, Stacks, Course_Stacks
from django.views.generic import ListView, FormView
from .forms import CourseSearchForm
from django.db.models import Q
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    stack_list = Stacks.objects.all()
    return render(request, 'index.html', {'stack_list': stack_list})

class Courselist(ListView):
    model = Course
    paginate_by = 20
    template_name ='course/list.html'
    ordering ='rank'

    # ListView를 사용할땐 get_context_data를 안해도 됨. 자동으로 해줌.
    # def get_context_data(self, **kwargs):
        # context = super(Courselist, self).get_context_data()
        # context['course'] = Course.objects.all()
        # return context

# search FBV형
def search(request):
    course_list = Course.objects.all()
    search = request.GET.get('search','')
    if search:
        search_list = course_list.filter(
            Q(title__icontains=search) |
            Q(teacher__icontains=search) |
            Q(headline__icontains=search) |
            Q(stack__name__icontains=search) 
        ).distinct()
        # print(search_list.query)

        # print(search_list[5].title)
    paginator = Paginator(search_list, 10)
    page = request.GET.get('page', '')
    course = paginator.get_page(page)

    return render(request, 'course/course_search.html',{'course':course, 'search':search})