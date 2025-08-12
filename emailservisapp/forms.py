import os

from django.forms import ModelForm
from .models import Client, Message, Mailing, Attempt
from django.core.exceptions import ValidationError

class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = ['email', 'name', 'comment']

    def __init__(self, *args, **kwargs):
        super(ClientForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({'class': 'form-control',
                                                 'placeholder': 'Введите почту получателя'})
        self.fields['name'].widget.attrs.update({'class': 'form-control',
                                                 'placeholder': 'Введите имя получателя'})
        self.fields['comment'].widget.attrs.update({'class': 'form-control',
                                                 'placeholder': 'Добавьте комментарий'})
        # self.fields['owner'].widget.attrs.update({'class': 'form-control', })

class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ['subject', 'body']

    def __init__(self, *args, **kwargs):
        super(MessageForm, self).__init__(*args, **kwargs)
        self.fields['subject'].widget.attrs.update({'class': 'form-control',
                                                 'placeholder': 'Введите тему сообщения'})
        self.fields['body'].widget.attrs.update({'class': 'form-control',
                                                 'placeholder': 'Введите само сообщение'})

class MailingForm(ModelForm):
    class Meta:
        model = Mailing
        fields = ['status_mailing', 'message', 'clients']

    def __init__(self, *args, **kwargs):
        super(MailingForm, self).__init__(*args, **kwargs)
        self.fields['status_mailing'].widget.attrs.update({'class': 'form-control',
                                                 'placeholder': 'Статус рассылки по умолчанию СОЗДАНА'})
        self.fields['message'].widget.attrs.update({'class': 'form-control',
                                                 'placeholder': 'Выберете сообщение для рассылки'})
        self.fields['clients'].widget.attrs.update({'class': 'form-control',
                                                    'placeholder': 'Выберете получателей для рассылки'})

class AttemptForm(ModelForm):
    class Meta:
        model = Attempt
        fields = ['mailing',]

    def __init__(self, *args, **kwargs):
        super(AttemptForm, self).__init__(*args, **kwargs)
        self.fields['mailing'].widget.attrs.update({'class': 'form-control',
                                                 'placeholder': 'Выберете рассылку'})
