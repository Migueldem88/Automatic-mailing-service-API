from django.contrib import admin
from .models import Mailing,Message


@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    list_display = ['id','subject','message_text']

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['id','sent_at']