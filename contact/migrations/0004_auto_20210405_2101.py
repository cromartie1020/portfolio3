# Generated by Django 3.1.7 on 2021-04-06 01:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0003_auto_20210405_2100'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='account_number1',
            new_name='account_number',
        ),
    ]
