from course import views
from django.urls import path

app_name = 'course'
urlpatterns = [
    # '/course/'
    path('', views.Courselist.as_view(), name='course'),
    # '/search.CBV
    # path('search/', views.Search.as_view(), name="search")
]