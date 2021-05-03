# Generated by Django 3.2 on 2021-04-28 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.CharField(max_length=25, unique=True)),
                ('full_name', models.CharField(max_length=200)),
                ('date_of_birth', models.DateField()),
                ('date_of_joined', models.DateField()),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('address', models.CharField(blank=True, max_length=200, null=True)),
                ('gender', models.CharField(choices=[('male', 'male'), ('female', 'female')], default='male', max_length=6)),
                ('status', models.BooleanField(choices=[(True, 'active'), (False, 'Inactive')], default=True)),
            ],
        ),
        migrations.CreateModel(
            name='StudentFamily',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=200)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('address', models.CharField(blank=True, max_length=200, null=True)),
                ('gender', models.CharField(choices=[('male', 'male'), ('female', 'female')], default='male', max_length=6)),
                ('relative_relation', models.CharField(blank=True, max_length=200, null=True)),
                ('status', models.BooleanField(choices=[(True, 'active'), (False, 'Inactive')], default=True)),
                ('student_id', models.ManyToManyField(related_name='Family', to='student.Student')),
            ],
        ),
    ]