# Generated by Django 4.0 on 2022-01-04 04:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('todo_list', '0002_priority_todoitem_created_date_todoitem_todo_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='priority',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
