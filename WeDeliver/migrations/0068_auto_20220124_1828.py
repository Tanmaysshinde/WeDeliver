# Generated by Django 3.2.4 on 2022-01-24 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WeDeliver', '0067_auto_20220124_1826'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='email_verification',
            field=models.CharField(choices=[('V', 'Verified'), ('NV', 'Not Verified')], max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='phone_no_verification',
            field=models.CharField(choices=[('V', 'Verified'), ('NV', 'Not Verified')], max_length=2, null=True),
        ),
    ]
