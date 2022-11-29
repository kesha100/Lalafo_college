from django.contrib.auth.models import AbstractUser
from django.db import models


class Category(models.Model):
    category_name = models.CharField(max_length=255, verbose_name='название категории')

    def __str__(self):
        return self.category_name


class Location(models.Model):
    city = models.CharField(max_length=255, verbose_name='город')

    def __str__(self):
        return self.city


class User(AbstractUser):
    picture = models.TextField(null=True, blank=True)
    phoneNumber = models.CharField(max_length=13, verbose_name='номер телефона')


class Product(models.Model):
    product = models.CharField(max_length=255, verbose_name='название продукта')
    price = models.PositiveIntegerField(verbose_name='стоимость')
    CURRENCY_CHOICES = [
        ('USD', "USD"),
        ('KGS', "KGS"),
    ]
    currency = models.CharField(max_length=3, verbose_name='валюта', choices=CURRENCY_CHOICES)
    picture = models.TextField(verbose_name='изображения')
    description = models.TextField(verbose_name='описание продукта')
    category = models.ForeignKey(Category, related_name='product_category', on_delete=models.PROTECT,
                                 verbose_name='категория')
    location = models.ForeignKey(Location, related_name='product_location', on_delete=models.PROTECT,
                                 verbose_name="город")
    user = models.ForeignKey(User, related_name='product_user', on_delete=models.CASCADE, verbose_name='пользователь')

    def user_id(self):
        return self.user.id
