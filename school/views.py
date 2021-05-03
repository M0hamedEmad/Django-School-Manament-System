from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    ListView
    )
from django.contrib.auth.mixins import LoginRequiredMixin
from django_filters.views import FilterView
from .models import ClassRoom, Course, Grade

# Start ClassRoom Views

class ClassRoomListView(LoginRequiredMixin, FilterView):
    model            = ClassRoom
    template_name    = 'school/class_room_list.html'
    filterset_fields = ('title', 'grade',)
        
    def get_paginate_by(self, queryset, *args, **kwargs):
        entries = self.request.GET.get('entries')
        paginate_by = entries if entries is not None else 25
        return paginate_by
        
      
class ClassRoomDetailView(LoginRequiredMixin, DetailView):
    model = ClassRoom
    template_name = 'school/class_room_detail.html'

class ClassRoomCreateView(LoginRequiredMixin, CreateView):
    model = ClassRoom
    fields = '__all__'
    template_name = 'school/class_room_form.html'
    
    def get_success_url(self, **kwargs):
        return reverse_lazy('class_room_detail', kwargs={"pk":self.object.id})

class ClassRoomUpdateView(LoginRequiredMixin, UpdateView):
    model = ClassRoom
    fields = '__all__'
    template_name = 'school/class_room_form.html'
    
    def get_success_url(self, **kwargs):
        return reverse_lazy('class_room_detail', kwargs={"pk":self.object.id})

class ClassRoomDeleteView(LoginRequiredMixin, DeleteView):
    model = ClassRoom
    template_name = 'school/class_room_confirm_delete.html'
    
    def get_success_url(self, **kwargs):
        return reverse_lazy('class_room')
   
    
# End ClassRoom Views

# Start Grade Views

class GradeListView(LoginRequiredMixin, FilterView):
    model            = Grade
    template_name    = 'school/grade_list.html'
    filterset_fields = ('title',)
        
    def get_paginate_by(self, queryset, *args, **kwargs):
        entries = self.request.GET.get('entries')
        paginate_by = entries if entries is not None else 25
        return paginate_by
        

class GradeCreateView(LoginRequiredMixin, CreateView):
    model = Grade
    fields = '__all__'
    template_name = 'school/grade_form.html'
    
    def get_success_url(self, **kwargs):
        return reverse_lazy('grade')

class GradeUpdateView(LoginRequiredMixin, UpdateView):
    model = Grade
    fields = '__all__'
    template_name = 'school/grade_form.html'
    
    def get_success_url(self, **kwargs):
        return reverse_lazy('grade')

class GradeDeleteView(LoginRequiredMixin, DeleteView):
    model = Grade
    template_name = 'school/class_room_confirm_delete.html'
    
    def get_success_url(self, **kwargs):
        return reverse_lazy('grade')
   
    
# End Grade Views

# Start Course Views

class CourseListView(LoginRequiredMixin, FilterView):
    model            = Course
    template_name    = 'school/grade_list.html'
    filterset_fields = ('title',)
    def get_paginate_by(self, queryset, *args, **kwargs):
        entries = self.request.GET.get('entries')
        paginate_by = entries if entries is not None else 25
        return paginate_by
        

class CourseCreateView(LoginRequiredMixin, CreateView):
    model = Course
    fields = '__all__'
    template_name = 'school/grade_form.html'
    
    def get_success_url(self, **kwargs):
        return reverse_lazy('course')

class CourseUpdateView(LoginRequiredMixin, UpdateView):
    model = Course
    fields = '__all__'
    template_name = 'school/grade_form.html'
    
    def get_success_url(self, **kwargs):
        return reverse_lazy('course')

class CourseDeleteView(LoginRequiredMixin, DeleteView):
    model = Course
    template_name = 'school/class_room_confirm_delete.html'
    
    def get_success_url(self, **kwargs):
        return reverse_lazy('course')
   
    
# End Course Views
