from django.db import models
from student.models import Student
from school.models import Course
import datetime

term_choices = [
    (1, 'First Term'),
    (2, 'Second Term')
]

class Result(models.Model):
    student = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True, related_name='result')
    subject = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)
    year    = models.IntegerField(default=datetime.date.today().year)
    term    = models.IntegerField(choices=term_choices)
    exam_score = models.IntegerField()
    subject_score = models.PositiveIntegerField()
    
    def __str__(self):
        return f"{self.student} result at {self.year}"