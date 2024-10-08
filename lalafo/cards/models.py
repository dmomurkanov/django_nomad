from django.db import models
from .utilts import CONDITION_CHOICES, CAR_BODY


class Category(models.Model):
    name = models.CharField('Название категории', max_length=50)
    icon = models.ImageField('Иконка', upload_to='category/icon')
    icon_mobile = models.ImageField('Иконка', upload_to='category/icon_mobile')
    order = models.PositiveIntegerField('Порядок', default=0)
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ('order', )

    def __str__(self):
        return self.name


class Item(models.Model):
    title = models.CharField('Заголовок', max_length=255, null=True)
    price = models.CharField('Цена', max_length=20)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='item')
    description = models.TextField('Описание',)
    is_like = models.BooleanField('Нравится', default=False)
    created_at = models.DateTimeField('Время создания')

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['created_at']

    def __str__(self):
        return self.title



class ItemImages(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='item_images')
    image = models.ImageField('Изображение', upload_to='item')
    image_mobile = models.ImageField('Изображение', upload_to='item')

    class Meta:
        verbose_name = 'Изображение товара'
        verbose_name_plural = 'Изображения товаров'

    def __str__(self):
        return f'Изоброжение - {self.item.title}'

class ItemParameters(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='parameters')
    condition = models.CharField('Состояние', max_length=255, choices=CONDITION_CHOICES)
    car_body = models.CharField('Кузов', max_length=255, choices=CAR_BODY)
    mileage = models.IntegerField('Пробег', default=0)