# Generated by Django 4.1.7 on 2023-04-22 21:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('voteapp', '0006_uploadimage_question'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='uploadimage',
            name='question',
        ),
    ]
