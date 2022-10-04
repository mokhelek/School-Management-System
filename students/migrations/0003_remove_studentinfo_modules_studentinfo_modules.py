# Generated by Django 4.0.4 on 2022-10-04 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_studentinfo_full_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentinfo',
            name='modules',
        ),
        migrations.AddField(
            model_name='studentinfo',
            name='modules',
            field=models.ManyToManyField(blank=True, related_name='modules', to='students.studentmodules'),
        ),
    ]
