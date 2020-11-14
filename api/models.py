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
    date = models.DateTimeField(blank=True)
    last_update = models.DateTimeField(blank=True)
    sent = models.IntegerField(blank=True)
# todo


class Template(models.Model):
    subject = models.CharField(max_length=100)
    text = models.TextField()
    attachment = models.FileField()
    # todo
    date = models.DateTimeField()
    last_update = models.DateTimeField()


class Email(models.Model):
    mailbox = models.ForeignKey('Mailbox', null=True, blank=True, on_delete=models.SET_NULL)
    template = models.ForeignKey('Template', null=True, blank=True, on_delete=models.SET_NULL)
    to = models.TextField()
    cc = models.TextField()
    bcc = models.TextField()
    reply_to = models.TextField()
    sent_date = models.DateTimeField(blank=True)
    date = models.DateTimeField(blank=True)
