# Generated by Django 4.2.7 on 2023-12-06 19:04

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ledger', '0004_remove_khach_owner'),
        ('datHen', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dathen',
            name='tech',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='ledger.technician'),
        ),
        migrations.AlterField(
            model_name='dathen',
            name='thoiLuong',
            field=models.DurationField(default=datetime.timedelta),
        ),
    ]
