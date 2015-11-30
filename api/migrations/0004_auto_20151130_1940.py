# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20151130_1726'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fillup',
            name='gallons',
            field=models.DecimalField(max_digits=5, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='fillup',
            name='miles',
            field=models.DecimalField(max_digits=5, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='fillup',
            name='pricePerGallon',
            field=models.DecimalField(max_digits=4, decimal_places=3),
        ),
    ]
