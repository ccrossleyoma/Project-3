# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fillup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField(auto_now_add=True)),
                ('miles', models.DecimalField(max_digits=3, decimal_places=2)),
                ('gallons', models.DecimalField(max_digits=3, decimal_places=2)),
                ('pricePerGallon', models.DecimalField(max_digits=3, decimal_places=3)),
            ],
            options={
                'verbose_name_plural': 'Fillups',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=40)),
                ('password', models.CharField(max_length=40)),
                ('fillups', models.ForeignKey(to='api.Fillup')),
            ],
            options={
                'verbose_name_plural': 'Users',
            },
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('year', models.DecimalField(max_digits=4, decimal_places=0)),
                ('make', models.CharField(max_length=40)),
                ('model', models.CharField(max_length=40)),
                ('trim', models.CharField(max_length=40)),
                ('fillups', models.ForeignKey(to='api.Fillup')),
            ],
            options={
                'verbose_name_plural': 'Vehicles',
            },
        ),
        migrations.AddField(
            model_name='user',
            name='vehicles',
            field=models.ForeignKey(to='api.Vehicle'),
        ),
    ]
