# Generated by Django 3.2 on 2021-04-29 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='image',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to='profile_pics'),
        ),
        migrations.AlterField(
            model_name='studentfamily',
            name='student_id',
            field=models.ManyToManyField(related_name='family', to='student.Student'),
        ),
    ]
