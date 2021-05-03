from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    ListView
    )
from django_filters.views import FilterView
from .models import ClassRoom, Course, Grade

# Start ClassRoom Views

class ClassRoomListView(FilterView):
    model            = ClassRoom
    template_name    = 'school/class_room_list.html'
    filterset_fields = ('title', 'grade',)
        
    def get_paginate_by(self, queryset, *args, **kwargs):
        entries = self.request.GET.get('entries')
        paginate_by = entries if entries is not None else 25
        return paginate_by
        
      
class ClassRoomDetailView(DetailView):
    model = ClassRoom
    template_name = 'school/class_room_detail.html'

class ClassRoomCreateView(CreateView):
    model = ClassRoom
    fields = '__all__'
    template_name = 'school/class_room_form.html'
    
    def get_success_url(self, **kwargs):
        return reverse_lazy('class_room_detail', kwargs={"pk":self.object.id})

class ClassRoomUpdateView(UpdateView):
    model = ClassRoom
    fields = '__all__'
    template_name = 'school/class_room_form.html'
    
    def get_success_url(self, **kwargs):
        return reverse_lazy('class_room_detail', kwargs={"pk":self.object.id})

class ClassRoomDeleteView(DeleteView):
    model = ClassRoom
    template_name = 'school/class_room_confirm_delete.html'
    
    def get_success_url(self, **kwargs):
        return reverse_lazy('class_room')
   
    
# End ClassRoom Views

# Start Grade Views

class GradeListView(FilterView):
    model            = Grade
    template_name    = 'school/grade_list.html'
    filterset_fields = ('title',)
        
    def get_paginate_by(self, queryset, *args, **kwargs):
        entries = self.request.GET.get('entries')
        paginate_by = entries if entries is not None else 25
        return paginate_by
        

class GradeCreateView(CreateView):
    model = Grade
    fields = '__all__'
    template_name = 'school/grade_form.html'
    
    def get_success_url(self, **kwargs):
        return reverse_lazy('grade')

class GradeUpdateView(UpdateView):
    model = Grade
    fields = '__all__'
    template_name = 'school/grade_form.html'
    
    def get_success_url(self, **kwargs):
        return reverse_lazy('grade')

class GradeDeleteView(DeleteView):
    model = Grade
    template_name = 'school/class_room_confirm_delete.html'
    
    def get_success_url(self, **kwargs):
        return reverse_lazy('grade')
   
    
# End Grade Views

# Start Course Views

class CourseListView(FilterView):
    model            = Course
    template_name    = 'school/grade_list.html'
    filterset_fields = ('title',)
    def get_paginate_by(self, queryset, *args, **kwargs):
        entries = self.request.GET.get('entries')
        paginate_by = entries if entries is not None else 25
        return paginate_by
        

class CourseCreateView(CreateView):
    model = Course
    fields = '__all__'
    template_name = 'school/grade_form.html'
    
    def get_success_url(self, **kwargs):
        return reverse_lazy('course')

class CourseUpdateView(UpdateView):
    model = Course
    fields = '__all__'
    template_name = 'school/grade_form.html'
    
    def get_success_url(self, **kwargs):
        return reverse_lazy('course')

class CourseDeleteView(DeleteView):
    model = Course
    template_name = 'school/class_room_confirm_delete.html'
    
    def get_success_url(self, **kwargs):
        return reverse_lazy('course')
   
    
# End Course Views
