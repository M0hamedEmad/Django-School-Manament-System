from django.urls import path
from .views import (
    AllRusltView,
    AllStudentResultDetailView,
    ResultDetailView,
    ResultCreateView,
    DetleteResultView,
)

urlpatterns = [
    path('', AllRusltView.as_view(), name='result_list'),
    path('<int:pk>/', AllStudentResultDetailView.as_view(), name='all_result'),
    path('<int:pk>/<int:year>/<int:term>/', ResultDetailView.as_view(), name='result'),
    path('create/', ResultCreateView.as_view(), name='result_create'),
    path('<int:pk>/<int:year>/<int:term>/delete/', DetleteResultView.as_view(), name='result_delete')
]
