# Generated by Django 4.2 on 2023-04-23 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("leavemanagement", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="student",
            name="phone",
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name="warden",
            name="phone",
            field=models.CharField(max_length=10),
        ),
    ]