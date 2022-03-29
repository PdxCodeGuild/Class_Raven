# Generated by Django 4.0 on 2022-01-07 01:36

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pics_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pic',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='users', to=settings.AUTH_USER_MODEL),
        ),
    ]
