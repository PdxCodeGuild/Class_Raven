# Generated by Django 3.2.7 on 2022-01-12 03:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0006_auto_20220112_0302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='priority_choice',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='todo_app.priority'),
        ),
    ]
