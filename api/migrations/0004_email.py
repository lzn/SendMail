# Generated by Django 3.1.3 on 2020-11-14 21:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20201114_2159'),
    ]

    operations = [
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('to', models.TextField()),
                ('cc', models.TextField()),
                ('bcc', models.TextField()),
                ('reply_to', models.TextField()),
                ('sent_date', models.DateTimeField(blank=True)),
                ('date', models.DateTimeField(blank=True)),
                ('mailbox', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.mailbox')),
                ('template', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.template')),
            ],
        ),
    ]