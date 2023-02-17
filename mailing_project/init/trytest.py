
from Mailing.applications.Messages.managers import MailingManager

from Mailing.applications.Messages.models import Mailing
# from ....applications.Messages.managers import MailingManager
# from ..applications.Messages.models import Mailing


mt = MailingManager.list_message_texts(Mailing.objects)
print(mt)