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


