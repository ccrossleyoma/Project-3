# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='fillups',
        ),
        migrations.RemoveField(
            model_name='user',
            name='password',
        ),
        migrations.RemoveField(
            model_name='user',
            name='vehicles',
        ),
        migrations.RemoveField(
            model_name='vehicle',
            name='fillups',
        ),
        migrations.AddField(
            model_name='fillup',
            name='vehicle',
            field=models.ForeignKey(to='api.Vehicle', null=True),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
