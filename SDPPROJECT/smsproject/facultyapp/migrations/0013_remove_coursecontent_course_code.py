# Generated by Django 5.0 on 2024-02-22 10:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('facultyapp', '0012_alter_coursecontent_course_code'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coursecontent',
            name='course_code',
        ),
    ]
