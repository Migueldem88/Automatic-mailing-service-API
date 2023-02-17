from __future__ import absolute_import,unicode_literals
from celery import shared_task
from django.core.mail import send_mail
from ..Messages.managers import MailingManager
from ..Messages.models import Mailing, Message

from django.core.mail import EmailMessage

from ..Client.managers import ClientManager
from ..Client.models import Client
from ... import settings



@shared_task()
def send_mail_func(ids,subject,text,filters,client_emails):

    if 'email' in filters:

        emails_from_Mailing= filters['email']
        for email in emails_from_Mailing:
            if email in client_emails:
                mail = EmailMessage(subject, text, settings.DEFAULT_FROM_EMAIL, [email], )
                mail.send(fail_silently=False)

                print(f"Message '{text}' sent to {email}")

                e_client_idd = int(Client.objects.filter(
                    email__iexact=email).values_list('id', flat=True)[0])
                new_message=Message(mailing_id=ids, sent=True, client_id=e_client_idd, )
                new_message.save()


            else:
                print(f"{email} not is in Clients")
    else:
        print("This mailing doesn't contain any mails")


    return ''

