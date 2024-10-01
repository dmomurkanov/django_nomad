# Generated by Django 4.2.16 on 2024-10-01 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='itemimages',
            options={'ordering': ['order'], 'verbose_name': 'Изображение товара', 'verbose_name_plural': 'Изображения товаров'},
        ),
        migrations.AddField(
            model_name='item',
            name='order',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='itemimages',
            name='order',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='category',
            name='order',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
