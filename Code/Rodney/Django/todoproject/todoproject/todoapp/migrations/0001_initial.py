# Generated by Django 4.0 on 2021-12-28 18:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Priority',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('priority_level', models.CharField(choices=[('HIGH', 'High'), ('MEDIUM', 'Medium'), ('LOW', 'Low')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='TodoItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_text', models.CharField(max_length=200)),
                ('created_date', models.DateTimeField(verbose_name='date created')),
                ('priority', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todoapp.priority')),
            ],
        ),
    ]
