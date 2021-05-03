from django.db import models
from student.models import Student
from staff.models import Staff

active_choices = [
    (True, 'active'),
    (False, 'inactive') 
]

class Grade(models.Model):
    title = models.CharField(max_length=200)
    
    def __str__(self):
        return self.title
    
class ClassRoom(models.Model):
    title    = models.CharField(max_length=200)
    capacity = models.IntegerField()
    grade    = models.ForeignKey(Grade, on_delete=models.SET_NULL, null=True)
    status   = models.BooleanField(default=True, choices=active_choices)
    students = models.ManyToManyField(Student)
    
    def __str__(self):
        return self.title
    
class Course(models.Model):
    title   = models.CharField(max_length=200)
    grade   = models.ManyToManyField(Grade)
    teachers = models.ManyToManyField(Staff)
    
    def __str__(self):
        return self.title
    
    