# Generated by Django 3.1.1 on 2020-10-29 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AuthApp', '0002_auto_20201030_0013'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='register',
            name='id',
        ),
        migrations.AddField(
            model_name='register',
            name='userid',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='register',
            name='mobile',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
