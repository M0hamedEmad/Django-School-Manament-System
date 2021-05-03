from django import forms
from django.forms.models import inlineformset_factory
from student.models import Student
from .models import Result

class ResultForm(forms.ModelForm):
    class Meta:
        model = Result
        fields = ('student', 'term', 'year')
        
ResultFormSet = inlineformset_factory(Student, Result, fields=('subject', 'exam_score', 'subject_score'), extra=8, can_delete=False)