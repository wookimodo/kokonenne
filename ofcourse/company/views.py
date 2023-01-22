from django.shortcuts import render
from django.views.generic import ListView,DetailView
from course.models import Company, Course_Stacks, Stacks
from django.db.models import Q
from django.core.paginator import Paginator


# Create your views here.
class CompanyList(ListView):
    model = Company
    template_name = 'company/main.html'

    ordering = 'pk'

    paginate_by = 9

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


# search FBV형2
# def search(request):
#     company_search_list = Company.objects.all()
#     search = request.GET.get('search','')
#     if search:
#         search_list = company_search_list.filter(
#             name__icontains=search
#         )
#     paginator = Paginator(search_list, 10)
#     page = request.GET.get('page', '')
#     company = paginator.get_page(page)

#     return render(request, 'company/main.html',{'company':company, 'search':search})



def search(request):
    company = Company.objects.all()
    search = request.GET.get('search','')

    if search:
        company_list = company.filter(name__icontains=search).distinct()
        return render(request, 'company/search.html', {'company':company_list, 'search':search})

    else:
        return render(request,  'company/search.html')