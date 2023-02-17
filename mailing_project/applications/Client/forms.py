from django import forms
from .models import Client

class ClientForm(forms.ModelForm):

    class Meta:
        model=Client
        fields = (
            'number',
            'op_code',
            'tag',
            'tz',
            'email',
        )
