from rest_framework import serializers, pagination
from .models import Mailing

class Mailing_serializer(serializers.ModelSerializer):

    class Meta:
        model = Mailing
        fields=(
            'id',
            'subject',
            'maling_start_time',
            'maling_finish_time',)

