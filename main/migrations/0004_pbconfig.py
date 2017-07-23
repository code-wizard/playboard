# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-23 05:13
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0003_pbsubdomains_link'),
    ]

    operations = [
        migrations.CreateModel(
            name='PbConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_creating', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_config', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'pb_config',
            },
        ),
    ]