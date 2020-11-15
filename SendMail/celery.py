import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'SendMail.settings')

app = Celery('SendMail')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
