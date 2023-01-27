from django.shortcuts import render
from django.views.generic import ListView,DetailView
from course.models import Company, Course_Stack, Stack
from django.db.models import Q
from django.core.paginator import Paginator


# Create your views here.
class CompanyList(ListView):
    model = Company
    template_name = 'company/company_list.html'

    ordering = 'pk'

    paginate_by = 15

    def get_context_data(self, **kwargs):
        context = super(CompanyList, self).get_context_data()
        context['stack'] = Stack.objects.all()

        filter = self.request.GET.get('filter','') #url의 쿼리스트링을 가져온다. 없는 경우 공백을 리턴한다

        if filter == 'foreign':
            context['object_list'] = Company.objects.filter(stack_info__iexact = '외국기업')
            context['page'] = 'filter'
        elif filter == 'comprehensive':
            context['object_list'] = Company.objects.filter(category__iexact = '종합 기업')
            context['page'] = 'filter'
        elif filter == 'social':
            context['object_list'] = Company.objects.filter(category__iexact = '소셜/컨텐츠 기업')
            context['page'] = 'filter'
        elif filter == 'ecommerce':
            context['object_list'] = Company.objects.filter(category__iexact = '이커머스 기업')
            context['page'] = 'filter'
        elif filter == 'trip':
            context['object_list'] = Company.objects.filter(category__iexact = '여행 기업')
            context['page'] = 'filter'
        elif filter == 'finance':
            context['object_list'] = Company.objects.filter(category__iexact = '금융/보험 기업')
            context['page'] = 'filter'
        elif filter == 'education':
            context['object_list'] = Company.objects.filter(category__iexact = '교육 기업')
            context['page'] = 'filter'
        elif filter == 'mobility':
            context['object_list'] = Company.objects.filter(category__iexact = '모빌리티 기업')
            context['page'] = 'filter'
        elif filter == 'foodtech':
            context['object_list'] = Company.objects.filter(category__iexact = '푸드테크 기업')
            context['page'] = 'filter'
        elif filter == 'realestate':
            context['object_list'] = Company.objects.filter(category__iexact = '부동산/인테리어 기업')
            context['page'] = 'filter'
        elif filter == 'healthcare':
            context['object_list'] = Company.objects.filter(category__iexact = '헬스케어 기업')
            context['page'] = 'filter'
        elif filter == 'ai':
            context['object_list'] = Company.objects.filter(category__iexact = '인공지능 기업')
            context['page'] = 'filter'
        elif filter == 'recruitment':
            context['object_list'] = Company.objects.filter(category__iexact = '직장 기업')
            context['page'] = 'filter'
        elif filter == 'etc':
            context['object_list'] = Company.objects.filter(category__iexact = '기타 기업')
            context['page'] = 'filter'

        return context


class Companydetail(DetailView):
    model = Company
    template_name = 'company/company_detail.html'

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
        return render(request, 'company/company_search.html', {'company':company_list, 'search':search})

    else:
        return render(request,  'company/company_search.html')




def filter(request):
    company_list = Company.objects.all()

    s = request.GET.getlist('s')
    ss = Q()

    if s:
        company_query = Q()
        for i in s:
            compnay_company_queryquery = company_query | Q(category__iexact=i)
        # com = company_list.filter(company_query)



    return render(request, 'company/filter.html',{'company_list' : company_list})