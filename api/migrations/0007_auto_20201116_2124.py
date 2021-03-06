# Generated by Django 3.1.3 on 2020-11-16 20:24

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20201116_2119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='email',
            name='cc',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.EmailField(blank=True, max_length=254), blank=True,  size=256),
        ),
        migrations.AlterField(
            model_name='email',
            name='reply_to',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AlterField(
            model_name='email',
            name='sent_date',
            field=models.DateTimeField(blank=True, default=None),
        ),
        migrations.AlterField(
            model_name='email',
            name='to',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.EmailField(blank=True, max_length=254), size=256),
        ),
    ]
