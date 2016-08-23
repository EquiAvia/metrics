# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-22 22:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dev_metrics', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReportingPeriod',
            fields=[
                ('reporting_period_id', models.AutoField(db_column='ReportingPeriodID', primary_key=True, serialize=False)),
                ('start_date', models.DateField(db_column='StartDate')),
                ('end_date', models.DateField(db_column='EndDate')),
            ],
            options={
                'ordering': ('start_date', 'end_date'),
                'verbose_name': 'Reporting Period',
                'verbose_name_plural': 'Reporting Periods',
                'db_table': 'ReportingPeriod',
                'managed': True,
            },
        ),
    ]