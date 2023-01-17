from django.shortcuts import render
from django.views.generic import DetailView
from course.models import Company, Course_Stacks, Stacks
from django.shortcuts import get_object_or_404

# Create your views here.


class StackDetail(DetailView):
    model = Stacks
    template_name = 'stack/stack_detail.html'

    def get_context_data(self, **kwargs):
        context = super(StackDetail, self).get_context_data()
        # context['company_detail_list'] = aaa.objects.all() # =>  aaa라는 테이블의 행을 다 가져오겠다
        print(context)
        return context