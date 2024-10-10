# Generated by Django 5.1.1 on 2024-10-08 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cards", "0003_itemparameters"),
    ]

    operations = [
        migrations.AddField(
            model_name="itemparameters",
            name="body_color",
            field=models.CharField(default="", max_length=100, verbose_name="Цвет"),
        ),
        migrations.AddField(
            model_name="itemparameters",
            name="car_body",
            field=models.CharField(
                choices=[("Седан", "sedan"), ("Минивен", "miniwen")],
                max_length=255,
                null=True,
                verbose_name="Кузов",
            ),
        ),
        migrations.AddField(
            model_name="itemparameters",
            name="engine_capacity",
            field=models.DecimalField(
                decimal_places=1,
                max_digits=10,
                null=True,
                verbose_name="Обьем двигателся",
            ),
        ),
        migrations.AddField(
            model_name="itemparameters",
            name="mileage",
            field=models.IntegerField(default=0, verbose_name="Пробег"),
        ),
        migrations.AddField(
            model_name="itemparameters",
            name="model",
            field=models.CharField(default="", max_length=255, verbose_name="Модель"),
        ),
        migrations.AddField(
            model_name="itemparameters",
            name="wheel_location",
            field=models.CharField(
                choices=[("Слева", "left"), ("Справа", "right"), ("Посередине", "mid")],
                max_length=100,
                null=True,
                verbose_name="расположение руля",
            ),
        ),
        migrations.AddField(
            model_name="itemparameters",
            name="year_of_manufacture",
            field=models.DateField(null=True, verbose_name="Год выпуска"),
        ),
        migrations.AlterField(
            model_name="itemparameters",
            name="condition",
            field=models.CharField(
                choices=[("Новый", "new"), ("Б/У", "used")],
                max_length=255,
                null=True,
                verbose_name="Состояние",
            ),
        ),
    ]
