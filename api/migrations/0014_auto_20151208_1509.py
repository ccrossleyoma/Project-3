# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_auto_20151208_0129'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fillup',
            old_name='pricePerGallon',
            new_name='pricepergallon',
        ),
        migrations.AlterField(
            model_name='fillup',
            name='date',
            field=models.DateField(),
        ),
    ]
