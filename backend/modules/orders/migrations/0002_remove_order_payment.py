# Generated by Django 4.2.5 on 2023-10-23 21:05

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("orders", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="order",
            name="payment",
        ),
    ]
