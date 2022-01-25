# Generated by Django 3.2.7 on 2022-01-14 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokedex_app', '0005_alter_pokemon_image_back_alter_pokemon_image_front'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='types',
            field=models.ManyToManyField(blank=True, related_name='type_name', to='pokedex_app.PokemonType'),
        ),
    ]
