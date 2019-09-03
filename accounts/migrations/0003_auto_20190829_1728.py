# Generated by Django 2.2.4 on 2019-08-29 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_remove_profile_public_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='africastalking_api_key',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='africastalking_sender_id',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='africastalking_username',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]