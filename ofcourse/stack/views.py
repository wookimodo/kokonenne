from django.shortcuts import render
from django.views.generic import ListView, DetailView
from course.models import Stack, Related_Stack, Company, Course_Stack
from django.shortcuts import get_object_or_404
from django.db.models import Q

# Create your views here.
class StackList(ListView): 
    model = Stack
    template_name = "stack/stack_list.html"
    ordering = 'pk'
    paginate_by = 12


class StackDetail(DetailView):
    model = Stack
    template_name = 'stack/stack_detail.html'

    def get_context_data(self, **kwargs):
        context = super(StackDetail, self).get_context_data()
        try:
            context['course'] = Course_Stack.objects.filter(stack_id=self.object.id).order_by('course__rank')[:5]
        except Exception as e:
            context['course'] = None

        return context

def search(request):
    stacks = Stack.objects.all()
    search = request.GET.get('search','')
    if search:
        stack_list = stacks.filter(
            Q(name__icontains=search) |
            Q(stack_dict__search_word__icontains=search)
        ).distinct()
        return render(request, 'stack/stack_search.html', {'stack':stack_list, 'search':search})
    else:
        return render(request,  'stack/stack_search.html')

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
