# Generated by Django 4.1.7 on 2023-04-22 19:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('voteapp', '0005_uploadimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploadimage',
            name='question',
            field=models.ForeignKey(default='0', on_delete=django.db.models.deletion.CASCADE, to='voteapp.question'),
            preserve_default=False,
        ),
    ]
