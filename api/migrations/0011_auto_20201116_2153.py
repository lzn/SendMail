# Generated by Django 3.1.3 on 2020-11-16 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_auto_20201116_2142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='email',
            name='sent_date',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
    ]