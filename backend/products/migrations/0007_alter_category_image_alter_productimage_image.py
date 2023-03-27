# Generated by Django 4.0.6 on 2023-03-15 09:49

from django.db import migrations, models
import products.models


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0006_category_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="category",
            name="image",
            field=models.ImageField(
                upload_to=products.models.PathAndRename("images/categories")
            ),
        ),
        migrations.AlterField(
            model_name="productimage",
            name="image",
            field=models.ImageField(
                upload_to=products.models.PathAndRename("images/products")
            ),
        ),
    ]
