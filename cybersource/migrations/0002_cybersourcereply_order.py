# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-29 11:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0004_auto_20160111_1108'),
        ('cybersource', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cybersourcereply',
            name='order',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cybersource_replies', to='order.Order'),
        ),
    ]
