# Generated by Django 4.2.7 on 2023-12-10 04:42

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('ledger', '0002_rename_ngayhen_khach_day_comes_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='khach',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None),
        ),
    ]
