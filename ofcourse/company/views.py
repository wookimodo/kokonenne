from django.shortcuts import render
from django.views.generic import ListView,DetailView
from course.models import Company, Course_Stack, Stack
from django.db.models import Q
from django.core.paginator import Paginator


# Create your views here.
class CompanyList(ListView):
    model = Company
    template_name = 'company/main.html'

    ordering = 'pk'

    paginate_by = 15

    # def get_context_data(self, **kwargs):
    #     context = super(CompanyList, self).get_context_data()
    #     context['company_list'] = Company.objects.all()
        
    #     return context

    

class Companydetail(DetailView):
    model = Company
    template_name = 'company/detail.html'

    def get_context_data(self, **kwargs):
        context = super(Companydetail, self).get_context_data()
        # context['company_detail'] = Company.objects.all()
        # context['id_values'] = Company.objects.filter(id=1)    

        return context




# 검색 함수
def search(request):
    company = Company.objects.all()
    search = request.GET.get('search','')

    if search:
        company_list = company.filter(
            Q(name__icontains=search) | # 회사 이름 검색
            Q(stack__name__iexact=search) |  # 스택 이름 검색
            Q(stack__stack_dict__search_word__iexact=search)  # 스택 사전에 있는 네임으로 검색   
        ).distinct()
        return render(request, 'company/search.html', {'company':company_list, 'search':search})

    else:
        return render(request,  'company/search.html')




def filter(request):
    company_list = Company.objects.all()

    f = request.GET.getlist('f')

    if f:
        fs = fs.filter(category__iexact=f)


    return render(request, 'company/filter.html',{'company_list' : company_list, 'stack' : f})

from django import template
register = template.Library()

@register.filter
def sub(value, arg):
    return value - arg
