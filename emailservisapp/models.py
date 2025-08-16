from django.db import models
from django.db.models import DateTimeField

from users.models import User


class Client(models.Model):
    email = models.EmailField(max_length=100, verbose_name='электронный адрес', unique=True)
    name = models.CharField(max_length=255, verbose_name='Ф.И.О.')
    comment = models.TextField(blank=True, null=True, verbose_name='Комментарий')
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, verbose_name='владелец', null=True, blank=True,
                              related_name='clients')


    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'
        ordering = ['email', 'name']


    def __str__(self):
        return f'Клиент {self.name} электронный адрес: {self.email}'


class Message(models.Model):
    subject = models.CharField(max_length=100, verbose_name='тема письма')
    body = models.TextField(blank=True, null=True, verbose_name='тело письма')
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, verbose_name='владелец', null=True, blank=True,
                              related_name='messages')

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
        ordering = ['subject', ]

    def __str__(self):
        return self.subject


class Mailing(models.Model):
    start = 'Создана'
    run = 'Запущена'
    end = 'Завершена'
    status_mailing_choices = [(start, 'Создана'), (run, 'Запущена'), (end, 'Завершена')]
    first_time = DateTimeField(blank=True, null=True, verbose_name='Дата и время первой отправки')
    last_time = DateTimeField(blank=True, null=True, verbose_name='Дата и время окончания отправки')
    status_mailing = models.CharField(max_length=10, choices=status_mailing_choices, default='Создана',
                                      verbose_name='статус рассылки')
    message = models.ForeignKey(Message, on_delete=models.SET_NULL, verbose_name='сообщение', null=True, blank=True,
                                related_name='mailing')
    clients = models.ManyToManyField(Client, related_name='mailing', verbose_name='получатели')
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, verbose_name='владелец', null=True, blank=True,
                              related_name='mailings')


    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'
        ordering = ['status_mailing', 'message']

    def __str__(self):
        return f'Рассылка сообщения: {self.message}'


class Attempt(models.Model):
    success = 'Успех'
    unsuccess = 'Провал'
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время попытки')
    status_attempt_choices = [(success, 'Успех'), (unsuccess, 'Провал')]
    status_attempt = models.CharField(max_length=10, choices=status_attempt_choices, verbose_name='статус попытки',
                                      null=True, blank=True)
    server_answer = models.TextField(blank=True, null=True, verbose_name='ответ сервера')
    mailing = models.ForeignKey(Mailing, on_delete=models.SET_NULL, verbose_name='рассылка', null=True, blank=True,
                                related_name='attempt')

    class Meta:
        verbose_name = 'Попытка рассылки'
        verbose_name_plural = 'Попытки рассылки'
        ordering = ['created_at', 'status_attempt']

    def __str__(self):
        return f'Попытка {self.attempt_id}'
