# Generated by Django 3.0.5 on 2020-05-09 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quaraDB', '0011_call_urgently'),
    ]

    operations = [
        migrations.AddField(
            model_name='call',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
