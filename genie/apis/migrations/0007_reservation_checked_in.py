# Generated by Django 3.1.6 on 2021-04-10 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0006_auto_20210410_1053'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='checked_in',
            field=models.BooleanField(default=False),
        ),
    ]