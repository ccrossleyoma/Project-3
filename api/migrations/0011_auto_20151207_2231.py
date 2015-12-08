# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_auto_20151207_2231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='vehicles',
            field=models.ManyToManyField(to='api.Vehicle', blank=True),
        ),
    ]
