# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-22 21:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bibliography', '0002_auto_20170222_1832'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fiction',
            name='author',
        ),
        migrations.RemoveField(
            model_name='press',
            name='author',
        ),
        migrations.AddField(
            model_name='text',
            name='ev_letter',
            field=models.CharField(choices=[('1', 'եւ'), ('2', 'և')], default='1', max_length=2),
        ),
        migrations.AlterField(
            model_name='text',
            name='author',
            field=models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.CASCADE, to='bibliography.Author'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='text',
            name='spelling',
            field=models.CharField(choices=[('modern_current', 'Արդի (1940-ներկա)'), ('modern_old', 'Արդի (1922-1940)'), ('classic', 'Դասական')], default='modern_current', max_length=20),
        ),
    ]