from stack import views
from django.urls import path

app_name = 'stack'

urlpatterns = [
    # '/stack/
    path('', views.StackList.as_view(), name="stack")
]