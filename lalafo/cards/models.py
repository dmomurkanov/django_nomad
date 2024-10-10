from django.db import models
from .utilts import CONDITION_CHOICES, CAR_BODY, WHEEL_LOCATION, TRANSMISSION


class Category(models.Model):
    name = models.CharField('Название категории', max_length=50)
    icon = models.ImageField('Иконка', upload_to='category/icon')
    icon_mobile = models.ImageField('Иконка для мобилы', upload_to='category/icon_mobile')
    order = models.PositiveIntegerField('Порядок', default=0)
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ('order', )


    def __str__(self):
        return self.name


class Item(models.Model):
    title = models.CharField('Заголовок', max_length=255, null=True)
    # image = models.ImageField()
    price = models.CharField('Цена', max_length=20)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='item')
    description = models.TextField('Описание',)
    is_like = models.BooleanField('Нравится', default=False)
    created_at = models.DateTimeField('Время создания')
    url = models.CharField('Ссылка в лалафо', max_length=1000, null=True, blank=True)


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
    condition = models.CharField('Состояние', max_length=255, choices=CONDITION_CHOICES, null=True)
    car_body = models.CharField('Кузов', max_length=255, choices=CAR_BODY, null=True)
    mileage = models.IntegerField('Пробег', default=0)
    body_color = models.CharField('Цвет', max_length=100, default='')
    release_date = models.DateField('Год выпуска', null=True)
    wheel_location = models.CharField('позиция руля', max_length=100, choices=WHEEL_LOCATION, null=True)
    engine_capacity = models.DecimalField('Обьем двигателя', max_digits=10, decimal_places=1, null=True)
    model = models.CharField('модель', max_length=255, default="")
    transmission = models.CharField('коробка передач', choices=TRANSMISSION, max_length=100, null=True)
    instock = models.BooleanField('В наличии', default=False)
