# Generated by Django 3.2 on 2021-04-29 14:50

from django.db import migrations, models
import student.models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_auto_20210429_1617'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='image',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to=student.models.image_upload),
        ),
    ]
