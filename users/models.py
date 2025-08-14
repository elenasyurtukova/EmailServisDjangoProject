from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='email')
    phone = models.CharField(max_length=15, verbose_name='телефон', blank=True, null=True,
                             help_text='Введите номер телефона')
    avatar = models.ImageField(upload_to='users/avatars/', blank=True, null=True, verbose_name='Аватар',
                               help_text='Загрузите свое фото')
    country = models.TextField(max_length=15, verbose_name='страна', blank=True, null=True,
                             help_text='Введите из какой вы страны')
    token = models.CharField(max_length=100, blank=True, null=True, verbose_name='Токен')
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.email