# Generated by Django 4.2.10 on 2024-02-22 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("homepage_core", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Friend",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                ("display_name", models.CharField(max_length=32)),
                ("url", models.URLField(max_length=64)),
            ],
        ),
    ]