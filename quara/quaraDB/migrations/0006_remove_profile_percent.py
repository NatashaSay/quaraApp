# Generated by Django 3.0.5 on 2020-05-09 11:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quaraDB', '0005_auto_20200509_1403'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='percent',
        ),
    ]