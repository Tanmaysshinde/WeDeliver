# Generated by Django 3.2.4 on 2022-01-26 10:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('WeDeliver', '0070_auto_20220126_1553'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='email_no_otp',
            new_name='email_otp',
        ),
    ]
