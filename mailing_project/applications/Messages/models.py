from django.db import models
from ..Client.models import Client
from django.utils import timezone

#managers
from .managers import MailingManager

class Mailing(models.Model):

    maling_start_time = models.DateTimeField()
    message_text = models.CharField(max_length=200)
    maling_finish_time = models.DateTimeField()
    subject=models.CharField(max_length=60,default='')
    client_filter=models.JSONField(default=dict)

    objects=MailingManager()

    def __str__(self):
        return str(self.id)+'---'+self.message_text

class Message(models.Model):
    sent_at=models.DateTimeField(default=timezone.now)
    mailing = models.ForeignKey(Mailing, on_delete=models.CASCADE)
    sent=models.BooleanField(default=False)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)


    def __str__(self):
        return str(self.id)+'---'+str(self.client)

