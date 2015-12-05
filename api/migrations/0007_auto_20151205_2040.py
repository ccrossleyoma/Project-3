# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import fuelup.api.validators


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20151205_2033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='make',
            field=models.CharField(max_length=40, validators=[fuelup.api.validators.removeJavascriptKeyword]),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='model',
            field=models.CharField(max_length=40, validators=[fuelup.api.validators.removeJavascriptKeyword]),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='trim',
            field=models.CharField(max_length=40, validators=[fuelup.api.validators.removeJavascriptKeyword]),
        ),
    ]
