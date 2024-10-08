# Generated by Django 5.1.1 on 2024-10-03 07:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cards", "0002_alter_itemimages_options_itemimages_order_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="ItemParameters",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "condition",
                    models.CharField(
                        choices=[("Новый", "new"), ("Б/У", "used")],
                        max_length=255,
                        verbose_name="Состояние",
                    ),
                ),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="parameters",
                        to="cards.category",
                    ),
                ),
            ],
        ),
    ]
