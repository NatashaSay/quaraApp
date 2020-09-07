# Generated by Django 3.0.5 on 2020-05-09 10:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('quaraDB', '0003_delete_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(blank=True, default='name', max_length=30)),
                ('lastname', models.CharField(blank=True, max_length=30)),
                ('age', models.IntegerField(blank=True, default=0)),
                ('birthdate', models.DateField(blank=True, null=True)),
                ('city', models.CharField(blank=True, max_length=30)),
                ('disrtict', models.CharField(blank=True, max_length=30)),
                ('address', models.CharField(blank=True, max_length=30)),
                ('percent', models.CharField(blank=True, max_length=30)),
                ('bio', models.TextField(blank=True, max_length=300)),
                ('image', models.ImageField(default='def.png', upload_to='profile_pics')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
