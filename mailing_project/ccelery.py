from __future__ import absolute_import, unicode_literals
from datetime import datetime
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mailing_project.settings')

import django
django.setup()


from celery import Celery
from celery.schedules import crontab

app = Celery('mailing_project')

app.conf.update(timezone = 'Turkey')

app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()

from .applications.Messages.managers import MailingManager
from .applications.Messages.models import Mailing

from .applications.Client.managers import ClientManager,ClienttestManager
from .applications.Client.models import Client

#We retrieve Mailing entities from our DB

#message_subjects:
subjects = MailingManager.list_message_subjects(Mailing.objects)

#message_texts
mt = MailingManager.list_message_texts(Mailing.objects)

#send_time
st= MailingManager.list_message_date(Mailing.objects)

#Client_filters
cf = MailingManager.list_clientfilters(Mailing.objects)

#We retrieve Client entities from our DB
clients_e_mails_list=ClientManager.list_client_emails(Client.objects)

ids = MailingManager.id_list(Mailing.objects)


obj={}
app.conf.beat_schedule = {}
for i in range(len(st)):
    obj['mailing'+str(i)]={'task':'mailing_project.applications.Messages.tasks.send_mail_func',
                           'schedule':crontab(hour=st[i].hour, minute=st[i].minute),
                           'args': (ids[i], subjects[i],mt[i],cf[i], clients_e_mails_list)}
app.conf.beat_schedule = obj


