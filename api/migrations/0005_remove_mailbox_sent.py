# Generated by Django 3.1.3 on 2020-11-16 08:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mailbox',
            name='sent',
        ),
    ]