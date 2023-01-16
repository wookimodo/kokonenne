from django.shortcuts import render
from .models import Course, Stacks, Course_Stacks
from django.views.generic import ListView, FormView
from .forms import CourseSearchForm
from django.db.models import Q

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
        context['course'] = Course.objects.all().order_by('rank')
        # context['stack'] = Stacks.objects.filter(name=Course.objects.get('stack'))
        print(context['course'].values('stack'))
        return context






# searchFormView
class SearchFormView(FormView):
    form_class = CourseSearchForm
    template_name = 'course/course_search.html'

    def form_valid(self, form):
        searchCourse = form.cleaned_data['search_course']
        c = Course.objects.all()
        # stack = Stacks.objects.values('stacks')
        # stack = [Stacks.objects.filter(urlid_id=i.urlid).values('urlid_id') for i in c ]
        # join =Course.objects.filter(urlid=Stacks.objects.values('urlid_id')).prefetch_related ('price')
        # cc = Course.objects.values()
        course_lst = Course.objects.filter(Q(title__icontains=searchCourse)  | Q(teacher__icontains=searchCourse) | Q(headline__icontains=searchCourse)).distinct()
        # co = Course.objects.values('stacks')
        # print(join.values())
        # Course.objects.filter(urlid=)
        a = Stacks.objects.values('urlid_id')
        for i in a:
            join =Course.objects.filter(urlid=i.values()).prefetch_related ('price')
            print(join.values())

        # a =Course.objects.filter(urlid=Stacks.objects.values('urlid_id')[2]).count()

        context  = {}
        context['form'] = form
        context['search'] = searchCourse
        context['object_list'] = course_lst
        return render(self.request, self.template_name, context)


    
