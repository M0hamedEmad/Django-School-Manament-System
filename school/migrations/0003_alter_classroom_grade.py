# Generated by Django 3.2 on 2021-05-01 12:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0002_auto_20210430_1550'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classroom',
            name='grade',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='school.grade'),
        ),
    ]