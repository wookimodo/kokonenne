from course import views
from django.urls import path

app_name = 'course'
urlpatterns = [
    # '/course/'
    path('', views.Courselist.as_view(), name='course'),
]