from django.contrib import admin
from play.models import Message


class MessageAdmin(admin.ModelAdmin):
    list_display = ('sender', 'sms', 'when', 'pin', 'game', 'amount', 'wins')


admin.site.register(Message, MessageAdmin)
