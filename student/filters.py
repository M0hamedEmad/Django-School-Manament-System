import django_filters
from .models import Student

class StudentFilter(django_filters.FilterSet):
    full_name = django_filters.CharFilter(lookup_expr='icontains', label='',)
    class Meta:
        model = Student
        fields = [
            'full_name',
        ]
    