# Generated by Django 2.0.2 on 2018-03-15 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='picture',
            field=models.ImageField(upload_to='img/artists/'),
        ),
    ]