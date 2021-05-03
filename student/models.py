from django.db import models
from PIL import Image

gender_choices = [
    ('male', 'male'),
    ('female', 'female'),
]

status_choices = [
    (True, 'active'),
    (False, 'Inactive'),
]

def image_upload(instance, file_name):
    """
    rename a pics photo to intance id

    Returns:
        [str]: [pass of image in media file]
    """
    _ , extention = file_name.split('.')
    return f"profil_pics/{instance.id}.{extention}"

class Student(models.Model):
    student_id = models.CharField(max_length=25, unique=True)
    full_name = models.CharField(max_length=200)
    date_of_birth = models.DateField()
    date_of_joined = models.DateField()
    phone = models.CharField(max_length=20, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    grade = models.ForeignKey('school.Grade', on_delete=models.SET_NULL, null=True)
    gender = models.CharField(max_length=6, choices=gender_choices, default='male')
    status = models.BooleanField(default=True, choices=status_choices)
    image = models.ImageField(null=True, blank=True, default="default.jpg", upload_to=image_upload)
    
    def __str__(self):
        return self.full_name
    
    def save(self, *args, **kwargs):
        """
            resize a large images and fix a problem when rename a image with id
        """
        
        # fix a problem when rename image by using id
        if self.pk is None:
            img = self.image
            self.image = None
            super().save(*args, **kwargs)
            self.image = img
        super().save(*args, **kwargs)
        
        # resize a large image
        image = Image.open(self.image.path)
        if image.width > 500 or image.height > 500:
            image.thumbnail( (500, 500) )
            image.save(self.image.path)
    
class StudentFamily(models.Model):
    full_name = models.CharField(max_length=200)
    phone = models.CharField(max_length=20, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    gender = models.CharField(max_length=6, choices=gender_choices, default='male')
    relative_relation = models.CharField(max_length=200, null=True, blank=True)
    status = models.BooleanField(default=True, choices=status_choices)
    student_id = models.ManyToManyField(Student, related_name='family')
    
    def __str__(self):
        return self.full_name
    