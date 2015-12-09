# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import fuelup.api.validators


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0014_auto_20151208_1509'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='make',
            field=models.CharField(max_length=15, validators=[fuelup.api.validators.removeJavascriptKeyword, fuelup.api.validators.checkHTML]),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='model',
            field=models.CharField(max_length=15, validators=[fuelup.api.validators.removeJavascriptKeyword, fuelup.api.validators.checkHTML]),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='trim',
            field=models.CharField(max_length=15, validators=[fuelup.api.validators.removeJavascriptKeyword, fuelup.api.validators.checkHTML]),
        ),
    ]
