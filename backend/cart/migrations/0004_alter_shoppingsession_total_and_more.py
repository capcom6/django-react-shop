# Generated by Django 4.0.6 on 2023-03-18 11:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("cart", "0003_alter_cartitem_session_alter_shoppingsession_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="shoppingsession",
            name="total",
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name="shoppingsession",
            name="user",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="shopping_session",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
