# Generated by Django 3.1.3 on 2020-11-14 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Template',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=100)),
                ('text', models.TextField()),
                ('attachement', models.FileField(upload_to='')),
                ('date', models.DateTimeField()),
                ('last_update', models.DateTimeField()),
            ],
        ),
    ]
