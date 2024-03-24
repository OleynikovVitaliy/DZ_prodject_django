from django.db import models


NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    category_name = models.CharField(max_length=100, verbose_name='Наименование категории')
    category_description = models.TextField(max_length=200, verbose_name='Описание категории')

    def __str__(self):
        return f'{self.category_name} {self.category_description}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    product_name = models.CharField(max_length=50, verbose_name='Наименование')
    description = models.TextField(max_length=300, verbose_name='Описание')
    preview = models.ImageField(upload_to='preview/', verbose_name='Изображение', **NULLABLE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    price = models.IntegerField(verbose_name='Цена за покупку')
    created_at = models.DateField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateField(auto_now=True, verbose_name='Дата последнего изменения')
    is_published = models.BooleanField(default=False, verbose_name='Опубликовано')

    def __str__(self):
        return f'{self.product_name} {self.description}'

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class Version(models.Model):

    number_version = models.IntegerField(default=1, verbose_name="Номер версии")
    name = models.CharField(max_length=100, verbose_name='Название версии')
    is_active = models.BooleanField(default=False, verbose_name='Активная версия')
    product = models.ForeignKey("Product", on_delete=models.CASCADE, verbose_name='Продукт')

    def __str__(self):
        return f'{self.number_version}'

    class Meta:
        verbose_name = 'Версия'
        verbose_name_plural = 'Версии'
