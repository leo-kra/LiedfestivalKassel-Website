# Generated by Django 2.0.2 on 2018-04-23 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0022_workshopreservation_ermaessigt'),
    ]

    operations = [
        migrations.AddField(
            model_name='concert',
            name='ticket_prices',
            field=models.CharField(default='', max_length=20),
        ),
    ]