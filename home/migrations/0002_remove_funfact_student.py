# Generated by Django 4.1.7 on 2023-06-19 17:49

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="funfact",
            name="student",
        ),
    ]
