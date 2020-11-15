from .models import Mailbox, Template, Email
from rest_framework import serializers
import logging


logger = logging.getLogger(__name__)


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


class EmailSerializer(serializers.HyperlinkedModelSerializer):
    def validate_mailbox(self, mailbox):
        if mailbox.is_active == False:
            raise serializers.ValidationError("Mailbox should be active")
        return mailbox

    class Meta:
        model = Email
        fields = ['mailbox', 'template', 'to' , 'cc', 'bcc', 'reply_to', 'sent_date', 'date'
        ]