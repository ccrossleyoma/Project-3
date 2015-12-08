# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_auto_20151207_2228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='vehicles',
            field=models.ManyToManyField(to='api.Vehicle', null=True),
        ),
    ]
