# Generated by Django 3.1.6 on 2021-03-21 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ordering', '0005_auto_20210320_1212'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordering',
            name='payment',
            field=models.CharField(default='NotDone', max_length=50),
        ),
    ]
