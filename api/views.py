from django.shortcuts import render
from rest_framework import viewsets,  mixins

from .filters import EmailFilter
from .models import Mailbox, Template, Email
from .serializers import MailboxSerializer, TemplateSerializer, EmailSerializer
from SendMail.tasks import send_email
import logging
# Create your views here.

logger = logging.getLogger(__name__)

class MailboxViewSet(viewsets.ModelViewSet):
    queryset = Mailbox.objects.all()
    serializer_class = MailboxSerializer


class TemplateViewSet(viewsets.ModelViewSet):
    queryset = Template.objects.all()
    serializer_class = TemplateSerializer


class EmailViewSet(mixins.CreateModelMixin,
                   mixins.ListModelMixin,
                   viewsets.GenericViewSet):
    queryset = Email.objects.all()
    serializer_class = EmailSerializer
    filterset_class = EmailFilter

    def perform_create(self, serializer):
        instance = serializer.save()
        logger.error("perform_create: " + str(instance.id))
        send_email.delay(instance.id)




