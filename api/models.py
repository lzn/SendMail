from django.contrib.postgres.fields import ArrayField
from django.db import models

# Create your models here.

class Mailbox(models.Model):
    host = models.CharField(max_length=200)
    port = models.IntegerField(default=465)
    login = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    email_from = models.CharField(max_length=50)
    use_ssl = models.BooleanField(default=True)
    is_active = models.BooleanField(blank=True, default=False)
    date = models.DateTimeField(blank=True, auto_now_add=True)
    last_update = models.DateTimeField(blank=True, auto_now=True)

    @property
    def sent(self):
        return Email.objects.filter(mailbox=self, sent_date__isnull=False).count()


class Template(models.Model):
    subject = models.CharField(max_length=100)
    text = models.TextField()
    attachment = models.FileField(blank=True, null=True)
    date = models.DateTimeField(blank=True)
    last_update = models.DateTimeField(blank=True, auto_now=True)


class Email(models.Model):
    mailbox = models.ForeignKey('Mailbox', null=True, blank=True, on_delete=models.SET_NULL)
    template = models.ForeignKey('Template', null=True, blank=True, on_delete=models.SET_NULL)
    to = ArrayField(models.EmailField(blank=True), size=256, blank=False, null=False)
    cc = ArrayField(models.EmailField(blank=True), size=256, blank=True, null=True)
    bcc = ArrayField(models.EmailField(blank=True), size=256, blank=True, null=True)
    reply_to = models.EmailField(blank=True, null=True, default=None)
    sent_date = models.DateTimeField(blank=True, default=None)
    date = models.DateTimeField(blank=True, auto_now_add=True)
