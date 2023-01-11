from django.shortcuts import render
from .models import Course, Stacks
from django.views.generic import ListView

# def list(requests):
#     # db에서 data query해서 오기
#     course = Course.objects.all()
#     stacks = Stacks.objects.all()
#     return render(requests, 'course/list.html', {"course":course, "stacks":stacks})

# Create your views here.

class Courselist(ListView):
    model = Course
    template_name ='course/list.html'

    def get_context_data(self, **kwargs):
        context = super(Courselist, self).get_context_data()
        context['course'] = Course.objects.all()
        context["stacks"] = Stacks.objects.filter(urlid_id=Course.urlid)
        # context["stacks"] = Stacks.objects.all()
        return context
