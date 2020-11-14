from .models import Mailbox, Template
from rest_framework import serializers

class MailboxSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Mailbox
        fields = ['host', 'port','login', 'password',
        'use_ssl', 'is_active', 'date' ,
        'last_update', 'sent'
        ]


class TemplateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Template
        fields = ['subject', 'text','attachment', 'date',
        'last_update'
        ]