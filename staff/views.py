from django.shortcuts import render, HttpResponse
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
from .filters import StaffFilter
from .models import Staff, JobType

# Start Staff Views

class StaffListView(LoginRequiredMixin, ListView):
    model               = Staff
    template_name       = 'staff/staff_list.html'
    context_object_name = 'staff'
  
    def get_queryset(self, *kwargs):
        filter = StaffFilter(self.request.GET, queryset= Staff.objects.all())
        return filter
        
      
class StaffDetailView(LoginRequiredMixin, DetailView):
    model = Staff
    context_object_name = 'staff'


class StaffCreateView(LoginRequiredMixin, CreateView):
    model = Staff
    fields = '__all__'
    
    def get_success_url(self, **kwargs):
        return reverse_lazy('staff_detail', kwargs={"pk":self.object.id})

class StaffUpdateView(LoginRequiredMixin, UpdateView):
    model = Staff
    fields = '__all__'

    def get_success_url(self, **kwargs):
        return reverse_lazy('staff_detail', kwargs={"pk":self.object.id})

class StaffDeleteView(LoginRequiredMixin, DeleteView):
    model = Staff
    context_object_name = 'staff'
    
    def get_success_url(self, **kwargs):
        return reverse_lazy('staff')
    
# End Staff Views


# Start Job Type Views

class JobTypeListView(LoginRequiredMixin, FilterView):
    model               = JobType
    template_name       = 'staff/job_type_filter.html'
    context_object_name = 'job_type'
    filterset_fields    = ['title']
        
    def get_paginate_by(self, queryset, *args, **kwargs):
        entries = self.request.GET.get('entries')
        paginate_by = entries if entries is not None else 25
        return paginate_by


class JobTypeCreateView(LoginRequiredMixin, CreateView):
    model = JobType
    template_name = 'staff/staff_form.html'
    fields = '__all__'

    def get_success_url(self, **kwargs):
        return reverse_lazy('job_type')

class JobTypeUpdateView(LoginRequiredMixin, UpdateView):
    model = JobType
    template_name = 'staff/staff_form.html'
    fields = '__all__'

    def get_success_url(self, **kwargs):
        return reverse_lazy('job_type')

class JobTypeDeleteView(LoginRequiredMixin, DeleteView):
    model = JobType
    context_object_name = 'staff'
    template_name = 'staff/staff_confirm_delete.html'
    
    def get_success_url(self, **kwargs):
        return reverse_lazy('job_type')
    
# End Job Type Views
