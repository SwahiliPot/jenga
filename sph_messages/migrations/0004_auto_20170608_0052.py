# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-06-07 21:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sph_messages', '0003_auto_20170608_0037'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sms',
            old_name='to',
            new_name='recipient_list',
        ),
        migrations.AddField(
            model_name='sms',
            name='recipient_count',
            field=models.CharField(blank=True, editable=False, max_length=10, null=True),
        ),
    ]
