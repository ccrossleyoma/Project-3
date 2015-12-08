# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0011_auto_20151207_2231'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fuelupuser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
                'verbose_name_plural': 'Users',
            },
        ),
        migrations.RemoveField(
            model_name='user',
            name='vehicles',
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.AddField(
            model_name='fuelupuser',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='fuelupuser',
            name='vehicles',
            field=models.ManyToManyField(to='api.Vehicle', blank=True),
        ),
    ]
