from __future__ import absolute_import
import managers
from .models import Mailing

a = managers.MailingManager.list_message_texts(Mailing.objects)
print(a)