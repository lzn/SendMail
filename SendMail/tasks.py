import logging
import smtplib, ssl
from datetime import datetime
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from celery import shared_task
from api.models import Email, Template, Mailbox


logger = logging.getLogger(__name__)


@shared_task(max_retries=3, autoretry_for=(Exception,), default_retry_delay=5)
def send_email(id):
    email = Email.objects.get(id=id)
    mailbox = email.mailbox
    template = email.template
    try:
        server = connect_to_server(mailbox.host, mailbox.port, mailbox.login, mailbox.password, mailbox.use_ssl)
        sendmail(server, template, email, mailbox)
        email.sent_date = datetime.now()
        email.save()
        server.quit()
    except Exception as e:
        logger.error("ERROR during email send ")
        logger.error(e)
        raise e

    return "Email " + str(email.id) + " sent successfully"


def connect_to_server(host, port, login, password, use_ssl):
    try:
        if use_ssl:
            server = smtplib.SMTP_SSL(host,port)
        else:
            server = smtplib.SMTP(host, port)

        server.login(login, password)
    except Exception as e:
        raise Exception(e)
    return server


def sendmail(server, template, email, mailbox):
    message = MIMEMultipart()
    message["From"] = mailbox.email_from
    message["To"] = ', '.join(email.to)
    rcpt = email.to
    message["Subject"] = template.subject
    if email.bcc:
        rcpt += email.bcc
        message["Bcc"] = ', '.join(email.bcc)
    if email.cc:
        rcpt += email.cc
        message["Cc"] = ', '.join(email.cc)

    message.attach(MIMEText(template.text, "plain"))
    if template.attachment.name:
        with open(template.attachment.name, "rb") as attachment:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())
        encoders.encode_base64(part)

        part.add_header(
            "Content-Disposition",
            f"attachment; filename= {template.attachment.name}"
        )
        message.attach(part)

    text = message.as_string()
    try:
        server.sendmail(mailbox.email_from, rcpt, text)
    except Exception as e:
        raise Exception(e)
