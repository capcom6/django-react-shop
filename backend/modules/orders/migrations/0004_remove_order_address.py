# Generated by Django 4.2.5 on 2023-11-02 19:16

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("orders", "0003_order_status"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="order",
            name="address",
        ),
    ]
