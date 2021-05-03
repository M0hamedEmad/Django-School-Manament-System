import django_filters
from .models import Staff

class StaffFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Staff
        fields = ['name', 'job_type']
