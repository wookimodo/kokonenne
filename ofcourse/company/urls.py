from company import views
from django.urls import path

app_name = 'company'

urlpatterns = [

    # '/company/
    path('', views.CompanyList.as_view(), name='company'),

    # # company_detail
    # path('<str:pk>/',views.Companydetail.as_view(), name='company_detail'),
    
]