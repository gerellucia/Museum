# Generated by Django 3.0.4 on 2020-04-14 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_exhibit_nfc_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='exhibit',
            name='audio',
            field=models.FileField(blank=True, upload_to='audio/'),
        ),
    ]
