# Generated by Django 4.0 on 2021-12-30 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_alter_priority_priority_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todoitem',
            name='completed_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
