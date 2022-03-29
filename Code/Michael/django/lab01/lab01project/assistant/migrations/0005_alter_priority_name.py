# Generated by Django 3.2.10 on 2022-03-06 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("assistant", "0004_alter_priority_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="priority",
            name="name",
            field=models.CharField(
                choices=[(1, "High"), ("Medium", 2), ("Low", 3)],
                default="Medium",
                max_length=6,
            ),
        ),
    ]
