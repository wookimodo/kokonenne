from django.shortcuts import render
from .models import Course, Stacks, Course_Stacks
from django.views.generic import ListView, FormView
from .forms import CourseSearchForm
from django.db.models import Q
from django.core.paginator import Paginator

# Create your views here.

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



# search FBV형2

# def search(request):
#     if request.method =='POST':
#         searched=request.POST['searched']
#         course = Course.objects.filter(Q(title__icontains=searched) | Q(teacher__icontains=searched) | Q(headline__icontains=searched)| Q(stack__name__icontains=searched))
#         return render(request,'course/course_search.html',{'searched':searched,'course':course})
#     else:
#         return render(request,'course/course_search.html',{})

# pagenation FBV형
# def listing(request):
#     # Pagenation을 시행할 객체를 가져오기
#     course_list = Course.objects.all().order_by('rank')
#     # 객체를 지정한 갯수만큼 Page단위로 저장, 여기서는 20개씩
#     paginator = Paginator(course_list, 20)
#     # request된 page를 저장
#     page_number = request.Get.get('page')
#     # request된 page의 인덱스를 저장
#     page_obj = paginator.get_page(page_number)
#     # 레코드를 template에 전달
#     return render(request, 'course/course_search.html', {'page_obj': page_obj})
    


# search CBV형
# class SearchFormView(FormView):
#     template_name = 'course/course_search.html'

#     def form_valid(self, form):
#         searchCourse = form.cleaned_data['search_course']
#         c = Course.objects.all()
#         course_lst = Course.objects.filter(Q(title__icontains=searchCourse)  | Q(teacher__icontains=searchCourse) | Q(headline__icontains=searchCourse) | Q(stack__icontains=searchCourse)).distinct()

#         context  = {}
#         context['form'] = form
#         context['search'] = searchCourse
#         context['object_list'] = course_lst
#         return render(self.request, self.template_name, context)

# search CBV형2
# class Search(ListView):
#     model = Course
#     paginate_by = 10
#     template_name = 'course/course_search.html'
#     ordering ='rank'

#     def get(self, request):
#         if request.method =='POST':
#             searched=request.POST['searched']
#             course = Course.objects.filter(Q(title__icontains=searched) | Q(teacher__icontains=searched) | Q(headline__icontains=searched)| Q(stack__name__icontains=searched))
#             return render(request,'course/course_search.html',{'searched':searched,'course':course})
#         else:
#             return render(request,'course/course_search.html',{})

