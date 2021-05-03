from django.urls import path
from .views import (StudentsListView,
                    StudentDetailView,
                    
                    StudentUpdateView,
                    StudentDeleteView,
                    StudentCreateView,
                    
                    StudentFamilysListView,
                    StudentFamilyDetailView,
                    
                    StudentFamilyUpdateView,
                    StudentFamilyDeleteView,
                    StudentFamilyCreateView)

urlpatterns = [
    path('', StudentsListView.as_view(), name='students_list'),
    path('<int:pk>/', StudentDetailView.as_view(), name='student'),
    
    path('create/', StudentCreateView.as_view(), name='create_student'),
    path('<int:pk>/update/', StudentUpdateView.as_view(), name='student_update'),
    
    path('<int:pk>/delete/', StudentDeleteView.as_view(), name='student_delete'),
    
    # student family urls
    path('family/', StudentFamilysListView.as_view(), name='student_family_list'),
    path('family/<int:pk>/', StudentFamilyDetailView.as_view(), name='student_family'),
    
    path('family/create/', StudentFamilyCreateView.as_view(), name='create_student_family'),
    path('<int:pk>/family/update/', StudentFamilyUpdateView.as_view(), name='student_family_update'),
    
    path('<int:pk>/family/delete/', StudentFamilyDeleteView.as_view(), name='student_family_delete'),
]