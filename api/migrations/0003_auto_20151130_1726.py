# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20151130_1715'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vehicle',
            name='user',
        ),
        migrations.AddField(
            model_name='user',
            name='vehicles',
            field=models.ForeignKey(to='api.Vehicle', null=True),
        ),
    ]
