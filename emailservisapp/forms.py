import os

from django.forms import ModelForm
from .models import Client
from django.core.exceptions import ValidationError

class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = ['email', 'name', 'comment', 'owner']

    def __init__(self, *args, **kwargs):
        super(ClientForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({'class': 'form-control',
                                                 'placeholder': 'Введите почту получателя'})
        self.fields['name'].widget.attrs.update({'class': 'form-control',
                                                 'placeholder': 'Введите имя получателя'})
        self.fields['comment'].widget.attrs.update({'class': 'form-control',
                                                 'placeholder': 'Добавьте комментарий'})
        self.fields['owner'].widget.attrs.update({'class': 'form-control', })
