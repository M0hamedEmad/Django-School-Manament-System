from django.db import models
from django.utils.timezone import now

gender_choices = [
    ('male', 'male'),
    ('female', 'female'),
]

status_choices = [
    (True, 'active'),
    (False, 'Inactive'),
]

class JobType(models.Model):
    title = models.CharField(max_length=70)
    
    def __str__(self):
        return self.title
        
class Staff(models.Model):
    name = models.CharField('full name', max_length=70)
    gender = models.CharField(max_length=6, choices=gender_choices)
    dob_date = models.DateField()
    date_of_appointment = models.DateField()
    salary = models.DecimalField(max_digits=6, decimal_places=2)
    phone = models.IntegerField(null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    job_type = models.ForeignKey(JobType, on_delete=models.SET_NULL, null=True)
    status = models.BooleanField(default=True, choices=status_choices)
    
    
    def __str__(self):
        return self.name