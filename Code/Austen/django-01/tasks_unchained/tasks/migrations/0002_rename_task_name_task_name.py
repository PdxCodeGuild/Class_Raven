# Generated by Django 4.0 on 2022-01-02 15:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='task_name',
            new_name='name',
        ),
    ]