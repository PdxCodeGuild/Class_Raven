# Generated by Django 4.0.1 on 2022-01-07 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_project_app', '0002_blogpost_date_edited'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='date_edited',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
