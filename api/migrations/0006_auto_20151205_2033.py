# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import fuelup.api.validators


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20151205_2030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fillup',
            name='gallons',
            field=models.DecimalField(max_digits=5, decimal_places=2, validators=[fuelup.api.validators.removeJavascriptKeyword]),
        ),
        migrations.AlterField(
            model_name='fillup',
            name='miles',
            field=models.DecimalField(max_digits=5, decimal_places=2, validators=[fuelup.api.validators.removeJavascriptKeyword]),
        ),
        migrations.AlterField(
            model_name='fillup',
            name='pricePerGallon',
            field=models.DecimalField(max_digits=4, decimal_places=3, validators=[fuelup.api.validators.removeJavascriptKeyword]),
        ),
    ]
