# Generated by Django 4.0 on 2021-12-28 01:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_alter_choice_question'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='status',
            field=models.CharField(choices=[('open', 'Open'), ('closed', 'Closed')], default='open', max_length=6),
        ),
    ]
