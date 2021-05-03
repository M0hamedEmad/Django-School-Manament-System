from django.urls import path
from .views import (
            ClassRoomListView,
            ClassRoomCreateView,
            ClassRoomDetailView,
            ClassRoomUpdateView,
            ClassRoomDeleteView,
            GradeListView,
            GradeCreateView,
            GradeUpdateView,
            GradeDeleteView,
            CourseListView,
            CourseCreateView,
            CourseUpdateView,
            CourseDeleteView,
)

urlpatterns = [
    # Class Room  Urls
    path('', ClassRoomListView.as_view(), name='class_room'),
    path('<int:pk>/', ClassRoomDetailView.as_view(), name='class_room_detail'),
    path('create/', ClassRoomCreateView.as_view(), name='class_room_create'),
    
    path('<int:pk>/edit/', ClassRoomUpdateView.as_view(), name='class_room_update'),
    
    path('<int:pk>/delete/', ClassRoomDeleteView.as_view(), name='class_room_delete'),
    
    # Grade  Urls
    path('grade/', GradeListView.as_view(), name='grade'),
    path('grade/create/', GradeCreateView.as_view(), name='grade_create'),
    
    path('grade/<int:pk>/edit/', GradeUpdateView.as_view(), name='grade_update'),
    
    path('grade/<int:pk>/delete/', GradeDeleteView.as_view(), name='grade_delete'),
    
    # Course  Urls
    path('course/', CourseListView.as_view(), name='course'),
    path('course/create/', CourseCreateView.as_view(), name='course_create'),
    
    path('course/<int:pk>/edit/', CourseUpdateView.as_view(), name='course_update'),
    
    path('course/<int:pk>/delete/', CourseDeleteView.as_view(), name='course_delete'),
    
]