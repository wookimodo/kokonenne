from django import forms

class CourseSearchForm(forms.Form):
    search_course = forms.CharField(label='Search Course')