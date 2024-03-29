# Generated by Django 4.2.9 on 2024-02-04 23:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="is_sales",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="product",
            name="sales_price",
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
    ]
