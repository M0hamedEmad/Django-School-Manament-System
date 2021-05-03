# Generated by Django 3.2 on 2021-04-30 00:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JobType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=70)),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70, verbose_name='full name')),
                ('gender', models.CharField(choices=[('male', 'male'), ('female', 'female')], max_length=6)),
                ('dob_date', models.DateField()),
                ('date_of_appointment', models.DateField()),
                ('salary', models.DecimalField(decimal_places=2, max_digits=6)),
                ('phone', models.IntegerField(blank=True, null=True)),
                ('address', models.CharField(blank=True, max_length=200, null=True)),
                ('status', models.BooleanField(choices=[(True, 'active'), (False, 'Inactive')], default=True)),
                ('job_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='staff.jobtype')),
            ],
        ),
    ]
