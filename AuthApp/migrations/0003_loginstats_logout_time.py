# Generated by Django 3.1.1 on 2020-11-01 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AuthApp', '0002_auto_20201031_1846'),
    ]

    operations = [
        migrations.AddField(
            model_name='loginstats',
            name='logout_time',
            field=models.FloatField(null=True),
        ),
    ]
