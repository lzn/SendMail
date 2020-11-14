from django.shortcuts import render
from rest_framework import viewsets
from .models import Mailbox, Template
from .serializers import MailboxSerializer, TemplateSerializer
# Create your views here.


class MailboxViewSet(viewsets.ModelViewSet):
    queryset = Mailbox.objects.all()
    serializer_class = MailboxSerializer


class TemplateViewSet(viewsets.ModelViewSet):
    queryset = Template.objects.all()
    serializer_class = TemplateSerializer
