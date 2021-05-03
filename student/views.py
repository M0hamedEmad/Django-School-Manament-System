from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import (DetailView,
                                  UpdateView,
                                  DetailView,
                                  DeleteView,
                                  CreateView,)

from django_filters.views import FilterView
from .models import Student, StudentFamily
from .filters import StudentFilter
    
# student views
class StudentsListView(FilterView):
    model = Student
    template_name = 'student/student_list.html'
    context_object_name = 'students'
    filterset_class = StudentFilter
    
    def get_paginate_by(self, queryset, *args, **kwargs):
        entries = self.request.GET.get('entries')
        paginate_by = entries if entries is not None else 25
        return paginate_by
    
class StudentDetailView(DetailView):
    model = Student
    context_object_name = 'student'
    
    
class StudentCreateView(CreateView):
    model = Student
    context_object_name = 'student'
    fields = '__all__'
    
    def get_success_url(self, **kwargs):
        return reverse_lazy('student', kwargs={'pk': self.object.id})
    

    
class StudentUpdateView(UpdateView):
    model = Student
    context_object_name = 'student'
    fields = '__all__'

    def get_success_url(self, **kwargs):
        return reverse_lazy('student', kwargs={'pk': self.object.id})
    
class StudentDeleteView(DeleteView):
    model = Student
    context_object_name = 'student'
    success_url = reverse_lazy('student_list')
# student family views  
      
class StudentFamilysListView(FilterView):
    model = StudentFamily
    template_name = 'student/student_list.html'
    context_object_name = 'students'
    filterset_class = StudentFilter
    
    def get_paginate_by(self, queryset, *args, **kwargs):
        entries = self.request.GET.get('entries')
        paginate_by = entries if entries is not None else 25
        return paginate_by
    
class StudentFamilyDetailView(DetailView):
    model = StudentFamily
    context_object_name = 'student'
    template_name = 'student/student_detail.html'
    
    
    
class StudentFamilyCreateView(CreateView):
    model = StudentFamily
    context_object_name = 'student'
    fields = '__all__'
    template_name = 'student/student_form.html'
    
    def get_success_url(self, **kwargs):
        return reverse_lazy('student_family', kwargs={'pk': self.object.id})
    

    
class StudentFamilyUpdateView(UpdateView):
    model = StudentFamily
    context_object_name = 'student_family'
    fields = '__all__'
    template_name = 'student/student_form.html'

    def get_success_url(self, **kwargs):
        return reverse_lazy('student_family', kwargs={'pk': self.object.id})
    
class StudentFamilyDeleteView(DeleteView):
    model = StudentFamily
    context_object_name = 'student'
    template_name = 'student/student_confirm_delete.html'
    success_url = reverse_lazy('student_family_list')
    