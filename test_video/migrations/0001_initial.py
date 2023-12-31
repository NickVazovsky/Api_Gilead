# Generated by Django 4.2.2 on 2023-07-26 10:26

from django.db import migrations, models
import test_video.models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Video",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("slug", models.SlugField()),
                ("description", models.CharField(max_length=255)),
                (
                    "picture",
                    models.FileField(
                        upload_to=test_video.models.video_upload_to,
                        verbose_name="Видео",
                    ),
                ),
            ],
        ),
    ]
