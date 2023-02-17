from django.db import models

class ClientManager(models.Manager):
    """Managers for Client(email)"""
    def list_client_emails(self):
        e_mail=self.values_list('email', flat=True)
        return list(e_mail)


class ClienttestManager(models.Manager):
    """Managers for Client(email)"""
    def ltest(self):
        e_mail = self.values_list('email', flat=True)
        return e_mail
        # e_mail=self.values_list('email', flat=True).get(pk=1)
        # return e_macdil