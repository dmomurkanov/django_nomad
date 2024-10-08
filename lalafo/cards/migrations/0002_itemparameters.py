# Generated by Django 5.1.1 on 2024-10-03 14:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemParameters',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('condition', models.CharField(choices=[('Новый', 'new'), ('Б/У', 'used')], max_length=255, verbose_name='Состояние')),
                ('car_body', models.CharField(choices=[('Минивен', 'Седан')], max_length=255, verbose_name='Кузов')),
                ('mileage', models.IntegerField(default=0, verbose_name='Пробег')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='parameters', to='cards.category')),
            ],
        ),
    ]
