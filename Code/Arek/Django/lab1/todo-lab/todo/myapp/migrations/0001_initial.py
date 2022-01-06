# Generated by Django 4.0 on 2022-01-04 03:15

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
                ('name', models.CharField(choices=[('high', 'High'), ('medium', 'Medium'), ('low', 'Low')], max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='Todoitem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=200)),
                ('created_date', models.DateTimeField(blank=True, null=True)),
                ('priority', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.priority')),
            ],
        ),
    ]
