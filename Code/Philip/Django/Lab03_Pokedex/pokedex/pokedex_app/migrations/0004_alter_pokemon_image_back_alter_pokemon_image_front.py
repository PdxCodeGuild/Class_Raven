# Generated by Django 4.0.1 on 2022-01-14 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokedex_app', '0003_alter_pokemon_height_alter_pokemon_image_back_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='image_back',
            field=models.ImageField(blank=True, upload_to=True),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='image_front',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]
