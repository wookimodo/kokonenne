from stack import views
from django.urls import path

app_name = 'stack'

urlpatterns = [
    # '/stack/

    # stack_detail
    path('<int:pk>/',views.StackDetail.as_view(), name='stack_detail')
]