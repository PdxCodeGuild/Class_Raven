# Generated by Django 4.0 on 2022-01-04 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_list', '0003_priority_created_date'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Priority',
        ),
        migrations.AddField(
            model_name='todoitem',
            name='priority',
            field=models.CharField(choices=[('high', 'High'), ('medium', 'Medium'), ('low', 'Low')], default='medium', max_length=6),
        ),
    ]
