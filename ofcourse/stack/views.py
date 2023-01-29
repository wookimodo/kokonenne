from django.shortcuts import render
from django.views.generic import ListView, DetailView
from course.models import Stack, Related_Stack, Company, Course_Stack
from django.shortcuts import get_object_or_404
from django.db.models import Q

# Create your views here.
class StackList(ListView): 
    model = Stack
    template_name = "stack/stack_list.html"
    ordering = '?'
    paginate_by = 12

    def get_context_data(self, **kwargs):
        context = super(StackList, self).get_context_data()
        context['stack'] = Stack.objects.all()

        filter = self.request.GET.get('filter','') #url의 쿼리스트링을 가져온다. 없는 경우 공백을 리턴한다

        if filter == 'frontend':
            context['object_list'] = Stack.objects.filter(assort__iexact = '프론트엔드')
            context['page'] = 'filter'
        elif filter == 'backend':
            context['object_list'] = Stack.objects.filter(assort__iexact = '백엔드')
            context['page'] = 'filter'
        elif filter == 'database':
            context['object_list'] = Stack.objects.filter(assort__iexact = '데이터베이스')
            context['page'] = 'filter'
        elif filter == 'DevOps':
            context['object_list'] = Stack.objects.filter(assort__iexact = '데브옵스')
            context['page'] = 'filter'
        elif filter == 'Language':
            context['object_list'] = Stack.objects.filter(assort__iexact = '언어')
            context['page'] = 'filter'
        elif filter == 'data':
            context['object_list'] = Stack.objects.filter(assort__iexact = '데이터')
            context['page'] = 'filter'
        elif filter == 'TestingTool':
            context['object_list'] = Stack.objects.filter(assort__iexact = '테스팅툴')
            context['page'] = 'filter'
        elif filter == 'businessTool':
            context['object_list'] = Stack.objects.filter(assort__iexact = '협업툴')
            context['page'] = 'filter'
        elif filter == 'mobile':
            context['object_list'] = Stack.objects.filter(assort__iexact = '모바일')
            context['page'] = 'filter'

        return context


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
            Q(stack_dict__search_word__iexact=search)
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
