from stack import views
from django.urls import path

app_name = 'stack'

urlpatterns = [
    # '/stack/
    path('',views.StackList.as_view(), name='stack_list'),
    # stack_detail
    path('<int:pk>/',views.StackDetail.as_view(), name='stack_detail'),
]