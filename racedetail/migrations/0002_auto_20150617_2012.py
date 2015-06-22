# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('racedetail', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='racedetail',
            name='raceDate',
            field=models.DateTimeField(null=True, default=django.utils.timezone.now, blank=True),
        ),
    ]
