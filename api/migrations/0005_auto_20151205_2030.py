# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import fuelup.api.validators


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20151130_1940'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fillup',
            name='vehicle',
            field=models.ForeignKey(validators=[fuelup.api.validators.removeJavascriptKeyword], to='api.Vehicle', null=True),
        ),
    ]
