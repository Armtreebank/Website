# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-19 00:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tokenization', '0019_verb_voice_a'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='verb',
            name='voice_a',
        ),
        migrations.AlterField(
            model_name='verb',
            name='voice',
            field=models.CharField(choices=[('1', 'ՉԲ'), ('2', 'ՆԲ')], default='1', max_length=5),
        ),
    ]
