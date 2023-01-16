from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import Company, CompanyDetail
from django.shortcuts import get_object_or_404

# Create your views here.
class CompanyList(ListView):
    model = Company
    template_name = 'company/main.html'

    ordering = 'pk'

    paginate_by = 12

    def get_context_data(self, **kwargs):
        context = super(CompanyList, self).get_context_data()
        context['company_list'] = Company.objects.all()
        
        return context

    

class Companydetail(DetailView):
    model = CompanyDetail
    template_name = 'company/company_detail.html'

    def get_context_data(self, **kwargs):
        context = super(Companydetail, self).get_context_data()
        context['company_detail_list'] = CompanyDetail.objects.all()
        
        return context



def business_list(request):
   business_list = Business.objects.all().order_by('-id') #데이터 역순 정렬
   page = request.GET.get('page', '1') #GET 방식으로 정보를 받아오는 데이터
   paginator = Paginator(business_list, '2') #Paginator(분할될 객체, 페이지 당 담길 객체수)
   paginated_business_lists = paginator.get_page(page) #페이지 번호를 받아 해당 페이지를 리턴
   ctx = {'business_list':business_list,'paginated_business_lists':paginated_business_lists}

   return render(request, template_name='list.html', context=ctx)