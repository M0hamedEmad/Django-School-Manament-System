from django.urls import path
from .views import (
    StaffListView,
    StaffDetailView,
    StaffCreateView,
    StaffUpdateView,
    StaffDeleteView,
    
    JobTypeListView,
    JobTypeCreateView,
    JobTypeUpdateView,
    JobTypeDeleteView,
)

urlpatterns = [
    # Staff  Urls
    path('', StaffListView.as_view(), name='staff'),
    path('create/', StaffCreateView.as_view(), name='staff_create'),
    path('<int:pk>/', StaffDetailView.as_view(), name='staff_detail'),
    
    path('<int:pk>/edit/', StaffUpdateView.as_view(), name='staff_update'),
    
    path('<int:pk>/delete/', StaffDeleteView.as_view(), name='staff_delete'),
    
    # Job Type Urls
    
    path('job-type/', JobTypeListView.as_view(), name='job_type'),
    path('job-type/create/', JobTypeCreateView.as_view(), name='job_type_create'),
    
    path('job-type/<int:pk>/edit/', JobTypeUpdateView.as_view(), name='job_type_update'),
    
    path('job-type/<int:pk>/delete/', JobTypeDeleteView.as_view(), name='job_type_delete'),
]