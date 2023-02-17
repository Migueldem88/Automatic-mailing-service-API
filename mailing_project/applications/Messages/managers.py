from django.db import models

class MailingManager(models.Manager):
    """managers for Mailing (messages)"""
    def list_message_texts(self):
        mestext = self.values_list('message_text', flat=True)
        return mestext
    def list_message_date(self):
        st = self.values_list('maling_start_time', flat=True)
        return st
    def list_message_subjects(self):
        subjects= self.values_list('subject', flat=True)
        return subjects
    def list_clientfilters(self):
        cf = self.values_list('client_filter', flat=True)
        return list(cf)
    def id_list(self):
        ids= self.values_list('id', flat=True)
        return list(ids)
