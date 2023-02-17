from django import forms
from .models import Mailing,Client


class MailingForm(forms.ModelForm):
    client_filter = forms.JSONField(widget=forms.TextInput(attrs={"placeholder":
                                    '''{"email":["example@gmail.com"],"op_code":"type your code here"}'''
                                                                  }))

    class Meta:
        model=Mailing
        fields = (
            'maling_start_time',
            'subject',
            'message_text',
            'maling_finish_time',
            'client_filter',

        )


        widgets = {
            'maling_start_time': forms.DateTimeInput(format='%d/%m/%Y %H:%M',attrs={'type': 'datetime-local'}),
            'maling_finish_time': forms.DateTimeInput(format='%d/%m/%Y %H:%M',attrs={'type': 'datetime-local'}),
            }




def mails():
    mails = Client.objects.all().values("email").distinct()
    EMAIL_CHOICES = []
    for i in mails:
        EMAIL_CHOICES.append([i.get('email'),i.get('email')])
    return EMAIL_CHOICES

