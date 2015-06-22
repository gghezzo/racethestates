# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='raceDetail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('state', models.CharField(max_length=2)),
                ('raceName', models.CharField(max_length=200)),
                ('raceDate', models.DateTimeField(default=django.utils.timezone.now)),
                ('raceLink', models.URLField(blank=True, null=True)),
                ('results', models.TimeField(blank=True, null=True)),
                ('meta', models.TextField(blank=True, null=True)),
                ('runnerName', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
