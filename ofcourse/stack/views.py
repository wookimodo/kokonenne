from django.shortcuts import render
from django.views.generic import ListView
from course.models import Stacks, Related_Stacks

# Create your views here.
class StackList(ListView): 
    model = Stacks
    template_name = "stack-list.html"
    ordering = '-pk'


    def get_context_data(self, **kwargs):
        context = super(StackList, self).get_context_data()
        context['stack_list'] = Stacks.objects.all()

        return context




