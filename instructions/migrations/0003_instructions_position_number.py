# Generated by Django 4.2.2 on 2023-09-11 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("instructions", "0002_alter_instructions_options"),
    ]

    operations = [
        migrations.AddField(
            model_name="instructions",
            name="position_number",
            field=models.PositiveIntegerField(
                default=1, verbose_name="Позиционный номер"
            ),
        ),
    ]
