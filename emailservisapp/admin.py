from django.contrib import admin
from .models import Client, Message, Mailing, Attempt

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "email", "comment")
    list_filter = ("name", "email")
    search_fields = ("name", "email")

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ("id", "subject", "body")
    search_fields = ("subject", "body")




