# Generated by Django 4.1.7 on 2023-04-24 02:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('voteapp', '0010_image_delete_uploadimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='question',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='voteapp.question'),
        ),
    ]
