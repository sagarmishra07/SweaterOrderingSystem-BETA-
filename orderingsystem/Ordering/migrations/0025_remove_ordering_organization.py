# Generated by Django 3.1.6 on 2021-04-23 06:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Ordering', '0024_auto_20210423_0827'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ordering',
            name='Organization',
        ),
    ]
