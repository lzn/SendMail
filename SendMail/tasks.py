import logging
import smtplib, ssl
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from celery import shared_task
from api.models import Email, Template, Mailbox


logger = logging.getLogger(__name__)

@shared_task
def send_email(id):
    logger.info("send_email task")
    email = Email.objects.get(id=id)
    mailbox = email.mailbox
    template = email.template
    try:
        logger.info("connect to server: " + mailbox.host + " " + str(mailbox.port)
                    + " " +  mailbox.login + " " + mailbox.password + " ")
        server = connect_to_server(mailbox.host, mailbox.port, mailbox.login, mailbox.password, mailbox.use_ssl)
        sendmail(server, template, email, mailbox)
        server.quit()
    except Exception as e:
        print(e)
        logger.error(e)

    return 'success email id:  ' + str(email.id) + " " + email.to + " " + template.subject + " " + mailbox.host


def connect_to_server(server, port, login, password, ssl):
    server = smtplib.SMTP(server, port)
    server.ehlo()
    if ssl:
        context = ssl.create_default_context()
        server.starttls(context=context)

    #server.login(login, password) #todo zahaszowane na czas developmentu

    logger.info("Connected to server")
    return server


def sendmail(server, template, email, mailbox):
    message = MIMEMultipart()
    message["From"] = mailbox.email_from
    message["To"] = email.to
    message["Subject"] = template.subject
    message["Bcc"] = email.bcc
    message["Cc"] = email.cc

    message.attach(MIMEText(template.text, "plain"))

    #todo czy attachment jest obowiazkowy ?
    with open(template.attachment, "rb") as attachment:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.ready())

    encoders.encode_base64(part)

    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {filename}"
    )

    message.attach(part)
    text = message.as_string()

    server.sendmail(mailbox.email_from, email.to, text)