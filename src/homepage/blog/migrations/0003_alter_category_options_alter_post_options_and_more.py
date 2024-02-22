# Generated by Django 4.2.10 on 2024-02-22 16:10

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("homepage_blog", "0002_alter_category_options"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="category",
            options={"ordering": ["name"], "verbose_name_plural": "Categories"},
        ),
        migrations.AlterModelOptions(
            name="post",
            options={"ordering": ["created_at"]},
        ),
        migrations.AddField(
            model_name="post",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="post",
            name="modified_at",
            field=models.DateTimeField(auto_now=True),
        ),
    ]