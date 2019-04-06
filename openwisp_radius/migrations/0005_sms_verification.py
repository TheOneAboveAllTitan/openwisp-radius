# Generated by Django 2.1.7 on 2019-04-03 17:16

from django.db import migrations, models

from .. import settings as app_settings


class Migration(migrations.Migration):

    dependencies = [
        ('openwisp_radius', '0004_default_permissions'),
        ('openwisp_users', '0005_user_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='organizationradiussettings',
            name='sms_verification',
            field=models.BooleanField(
                default=app_settings.DEFAULT_SMS_VERIFICATION,
                help_text=('whether users who sign up should be required to '
                           'verify their mobile phone number via SMS')),
        ),
    ]