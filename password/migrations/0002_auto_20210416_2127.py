# Generated by Django 3.1.7 on 2021-04-17 01:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('password', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='word',
            name='body',
            field=models.TextField(blank=True),
        ),
    ]
