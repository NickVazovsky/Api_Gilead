# Generated by Django 4.2.2 on 2023-08-08 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("account", "0005_useraccount_roles_remove_useraccount_groups_and_more"),
        ("test_video", "0002_typemedia_alter_video_slug_video_type_media"),
    ]

    operations = [
        migrations.AddField(
            model_name="video",
            name="content_for_roles",
            field=models.ManyToManyField(
                to="account.roles", verbose_name="Контент для"
            ),
        ),
    ]