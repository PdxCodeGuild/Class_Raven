# Generated by Django 4.0.1 on 2022-01-14 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokedex_app', '0004_alter_pokemon_image_back_alter_pokemon_image_front'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='image_back',
            field=models.ImageField(blank=True, upload_to='images_back'),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='image_front',
            field=models.ImageField(blank=True, upload_to='images_front/'),
        ),
    ]
