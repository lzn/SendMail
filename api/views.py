from django.shortcuts import render
from rest_framework import viewsets
from .models import Mailbox
from .serializers import MailboxSerializer
# Create your views here.

class MailboxViewSet(viewsets.ModelViewSet):
    queryset = Mailbox.objects.all()
    serializer_class = MailboxSerializer
