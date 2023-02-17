from django.db import models
from .managers import ClientManager
# Create your models here.
from timezone_field import TimeZoneField

class Client(models.Model):
    number = models.PositiveIntegerField()
    op_code = models.PositiveIntegerField()
    tag = models.CharField(max_length=30,blank=True,null=True)
    tz = TimeZoneField(use_pytz=True)
    email = models.EmailField(null=True, blank=True)

    objects=ClientManager()

    class Meta:
        verbose_name = 'Client info'
        verbose_name_plural = 'List of Clients'


    def __str__(self):
        return str(self.id) + '-'+str(self.tag)
