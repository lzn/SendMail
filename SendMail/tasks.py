import logging
from celery import shared_task
from api.models import  Email, Template, Mailbox


logger = logging.getLogger(__name__)

@shared_task
def send_email(id):
    logger.info("send_email task")
    email = Email.objects.get(id=id)
    mailbox = email.mailbox
    template = email.template
    return 'success email id:  ' +  str(email.id) + " " +  email.to + " " + template.subject + " " + mailbox.host