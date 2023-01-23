from django.shortcuts import render
from django.views.generic import ListView, DetailView
from course.models import Stacks, Related_Stacks, Company, Course_Stacks
from django.db.models import Q


# Create your views here.
class StackList(ListView): 
    model = Stacks
    template_name = "stack/stack_list.html"
    ordering = 'pk'
    paginate_by = 12


class StackDetail(DetailView):
    model = Stacks
    template_name = 'stack/stack_detail.html'

def search(request):
    stacks = Stacks.objects.all()
    search = request.GET.get('search','')
    if search:
        stack_list = stacks.filter(name__icontains=search).distinct()
        return render(request, 'stack/stack_search.html', {'stack':stack_list, 'search':search})
    else:
        return render(request,  'stack/stack_search.html')

