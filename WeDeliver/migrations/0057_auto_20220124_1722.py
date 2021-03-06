# Generated by Django 3.2.4 on 2022-01-24 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WeDeliver', '0056_auto_20220124_1722'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='flag',
        ),
        migrations.AddField(
            model_name='profile',
            name='email_verification',
            field=models.CharField(choices=[('V', 'Verified'), ('NV', 'Not Verified')], max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='phone_no_verification',
            field=models.CharField(choices=[('V', 'Verified'), ('NV', 'Not Verified')], max_length=10, null=True),
        ),
    ]
