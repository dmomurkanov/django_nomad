# Generated by Django 5.1.1 on 2024-10-01 07:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
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
                    "name",
                    models.CharField(max_length=50, verbose_name="Название категории"),
                ),
                (
                    "name_en",
                    models.CharField(
                        max_length=50, null=True, verbose_name="Название категории"
                    ),
                ),
                (
                    "name_ru",
                    models.CharField(
                        max_length=50, null=True, verbose_name="Название категории"
                    ),
                ),
                (
                    "name_ky",
                    models.CharField(
                        max_length=50, null=True, verbose_name="Название категории"
                    ),
                ),
                (
                    "icon",
                    models.ImageField(upload_to="category/icon", verbose_name="Иконка"),
                ),
                (
                    "icon_mobile",
                    models.ImageField(
                        upload_to="category/icon_mobile", verbose_name="Иконка"
                    ),
                ),
                (
                    "order",
                    models.PositiveIntegerField(default=0, verbose_name="Порядок"),
                ),
            ],
            options={
                "verbose_name": "Категория",
                "verbose_name_plural": "Категории",
                "ordering": ("order",),
            },
        ),
        migrations.CreateModel(
            name="Item",
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
                    "title",
                    models.CharField(
                        max_length=255, null=True, verbose_name="Заголовок"
                    ),
                ),
                ("price", models.CharField(max_length=20, verbose_name="Цена")),
                ("description", models.TextField(verbose_name="Описание")),
                (
                    "is_like",
                    models.BooleanField(default=False, verbose_name="Нравится"),
                ),
                ("created_at", models.DateTimeField(verbose_name="Время создания")),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="item",
                        to="cards.category",
                    ),
                ),
            ],
            options={
                "verbose_name": "Товар",
                "verbose_name_plural": "Товары",
                "ordering": ["created_at"],
            },
        ),
        migrations.CreateModel(
            name="ItemImages",
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
                    "image",
                    models.ImageField(upload_to="item", verbose_name="Изображение"),
                ),
                (
                    "image_mobile",
                    models.ImageField(upload_to="item", verbose_name="Изображение"),
                ),
                (
                    "item",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="item_images",
                        to="cards.item",
                    ),
                ),
            ],
            options={
                "verbose_name": "Изображение товара",
                "verbose_name_plural": "Изображения товаров",
            },
        ),
    ]
