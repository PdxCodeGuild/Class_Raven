# Generated by Django 4.0.3 on 2022-03-07 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('POKEDEX', '0004_ability_species_ability1_species_ability2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='species',
            name='attack',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='species',
            name='defense',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='species',
            name='height',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='species',
            name='hp',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='species',
            name='s_attack',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='species',
            name='s_defense',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='species',
            name='speed',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='species',
            name='weight',
            field=models.IntegerField(default=0),
        ),
    ]
