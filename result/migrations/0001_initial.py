# Generated by Django 3.2 on 2021-05-01 15:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('student', '0004_student_grade'),
        ('school', '0003_alter_classroom_grade'),
    ]

    operations = [
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField(default=2021)),
                ('term', models.IntegerField(choices=[(1, 'First Term'), (2, 'Second Term')])),
                ('exam_score', models.IntegerField()),
                ('subject_score', models.PositiveIntegerField()),
                ('student', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='result', to='student.student')),
                ('subject', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='school.course')),
            ],
        ),
    ]
