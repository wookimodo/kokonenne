from django.shortcuts import render
from django.views.generic import ListView, DetailView
from course.models import Stacks, Related_Stacks, Company, Course_Stacks
from django.shortcuts import get_object_or_404

# Create your views here.
class StackList(ListView): 
    model = Stacks
    template_name = "stack/stack_list.html"
    ordering = 'pk'
    paginate_by = 12


class StackDetail(DetailView):
    model = Stacks
    template_name = 'stack/stack_detail.html'

    # def get_context_data(self, **kwargs):
    #     context = super(StackDetail, self).get_context_data()
    #     st =Stacks.objects.filter(id=2).prefetch_related('company_set')[0]
    #     print(st)
    #     context['companies'] = st.course_set.all()
    #     print(context['companies'])
    #     for i in context['companies']:
    #         print("cours :", i)

        # context = super(StackDetail, self).get_context_data()
        # st =Stacks.objects.filter(id=2).prefetch_related('course_set')[0]
        # print(st)
        # context['courses'] = st.course_set.all()
        # print(context['courses'])
        # for i in context['courses']:
        #     print("cours :", i)
        
        # context['companies'] = Stacks.objects.filter(id=1).prefetch_related('company_set')
        # return context

    # def get_context_data(self, **kwargs):
    #     context = super(StackDetail, self).get_context_data()
    #     context['test'] = Company.objects.all()
    #     return context
