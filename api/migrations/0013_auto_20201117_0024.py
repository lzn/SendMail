# Generated by Django 3.1.3 on 2020-11-16 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_auto_20201116_2251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='template',
            name='attachment',
            field=models.FileField(blank=True, null=True, upload_to='uploads/'),
        ),
    ]