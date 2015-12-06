# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import fuelup.api.validators


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20151205_2040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fillup',
            name='date',
            field=models.DateField(auto_now_add=True, validators=[fuelup.api.validators.removeJavascriptKeyword]),
        ),
        migrations.AlterField(
            model_name='fillup',
            name='vehicle',
            field=models.ForeignKey(to='api.Vehicle', null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=20, validators=[fuelup.api.validators.removeJavascriptKeyword]),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='make',
            field=models.CharField(max_length=15, validators=[fuelup.api.validators.removeJavascriptKeyword]),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='model',
            field=models.CharField(max_length=15, validators=[fuelup.api.validators.removeJavascriptKeyword]),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='trim',
            field=models.CharField(max_length=15, validators=[fuelup.api.validators.removeJavascriptKeyword]),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='year',
            field=models.DecimalField(max_digits=4, decimal_places=0, validators=[fuelup.api.validators.removeJavascriptKeyword]),
        ),
    ]
