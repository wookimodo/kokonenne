from django.shortcuts import render
from django.views.generic import ListView, DetailView
<<<<<<< HEAD
from course.models import Stacks, Related_Stacks, Company, Course_Stacks
from django.db.models import Q

=======
from course.models import Stack, Related_Stack, Company, Course_Stack
from django.shortcuts import get_object_or_404
>>>>>>> 3917882cab3c1e13abc7c756b118ddc3f1db37ab

# Create your views here.
class StackList(ListView): 
    model = Stack
    template_name = "stack/stack_list.html"
    ordering = 'pk'
    paginate_by = 12


class StackDetail(DetailView):
    model = Stack
    template_name = 'stack/stack_detail.html'

<<<<<<< HEAD
def search(request):
    stacks = Stacks.objects.all()
    search = request.GET.get('search','')
    if search:
        stack_list = stacks.filter(name__icontains=search).distinct()
        return render(request, 'stack/stack_search.html', {'stack':stack_list, 'search':search})
    else:
        return render(request,  'stack/stack_search.html')

=======
    # def get_context_data(self, **kwargs):
    #     context = super(StackDetail, self).get_context_data()
    #     st =Stack.objects.filter(id=2).prefetch_related('company_set')[0]
    #     print(st)
    #     context['companies'] = st.course_set.all()
    #     print(context['companies'])
    #     for i in context['companies']:
    #         print("cours :", i)

        # context = super(StackDetail, self).get_context_data()
        # st =Stack.objects.filter(id=2).prefetch_related('course_set')[0]
        # print(st)
        # context['courses'] = st.course_set.all()
        # print(context['courses'])
        # for i in context['courses']:
        #     print("cours :", i)
        
        # context['companies'] = Stack.objects.filter(id=1).prefetch_related('company_set')
        # return context

    # def get_context_data(self, **kwargs):
    #     context = super(StackDetail, self).get_context_data()
    #     context['test'] = Company.objects.all()
    #     return context
>>>>>>> 3917882cab3c1e13abc7c756b118ddc3f1db37ab
