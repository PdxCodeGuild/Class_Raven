# Generated by Django 3.2.7 on 2022-01-12 03:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0005_priority_priority'),
    ]

    operations = [
        migrations.AlterField(
            model_name='priority',
            name='priority',
            field=models.CharField(choices=[('LOW', 'low'), ('MEDIUM', 'medium'), ('HIGH', 'high')], max_length=7),
        ),
        migrations.AlterField(
            model_name='todo',
            name='priority_choice',
            field=models.ForeignKey(blank=True, default='low', null=True, on_delete=django.db.models.deletion.CASCADE, to='todo_app.priority'),
        ),
    ]
