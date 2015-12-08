# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_auto_20151206_1957'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='vehicles',
        ),
        migrations.AddField(
            model_name='user',
            name='vehicles',
            field=models.ManyToManyField(to='api.Vehicle', blank=True),
        ),
    ]
