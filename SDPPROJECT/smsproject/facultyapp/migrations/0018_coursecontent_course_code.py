# Generated by Django 5.0 on 2024-02-22 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facultyapp', '0017_remove_coursecontent_course_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursecontent',
            name='course_code',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
    ]