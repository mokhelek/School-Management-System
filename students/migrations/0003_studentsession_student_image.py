# Generated by Django 4.0.4 on 2022-10-11 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_studentinfo_approved'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentsession',
            name='student_image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
