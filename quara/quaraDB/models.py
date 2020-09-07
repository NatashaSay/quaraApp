from django.db import models
from datetime import datetime as dt
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.exceptions import ObjectDoesNotExist
from PIL import Image, ImageDraw
from django.urls import reverse



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=30, blank=True, default='name')
    lastname = models.CharField(max_length=30, blank=True)
    age = models.IntegerField(default=0,blank=True)
    birthdate = models.DateField(null=True, blank=True)

    city = models.CharField(max_length=30, blank=True)
    district = models.CharField(max_length=30, blank=True)
    address = models.CharField(max_length=30, blank=True)

    percent = models.CharField(max_length=30, default='0', blank=True)

    bio = models.TextField(max_length=300, blank=True)
    image = models.ImageField(default='def.png', upload_to='profile_pics')


    def __str__(self):
        return f"{self.firstname} {self.lastname}"

    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 200 or img.width > 200:
            output_size = (200,200)
            img.thumbnail(output_size)
            img.save(self.image.path)


            draw = ImageDraw.Draw(img)
            draw.ellipse((180, 200, 180, 200), fill=(255,0,0,0))


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    try:
        instance.profile.save()
    except ObjectDoesNotExist:
        Profile.objects.create(user=instance)


class Control(models.Model):
    userprofile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True, blank=False)
    temperature = models.FloatField(blank=False)
    cough = models.BooleanField()
    headache = models.BooleanField()
    comment = models.TextField(max_length=300, blank=True)


class Call(models.Model):
    userprofile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True, blank=False)

    REASON = (
        ('t', 'Temperature'),
        ('h', 'Headache'),
        ('th', 'Throatache'),
        ('o', 'Other'),
    )

    reason = models.CharField(max_length=50, choices=REASON, blank=False, default=0)
    urgently = models.BooleanField(default=True)
    comment = models.TextField(max_length=300, blank=True)
    status = models.BooleanField(default=False)


class Statistics(models.Model):
    city_stat = models.CharField(max_length=30, blank=False)
    code = models.IntegerField(default=0,blank=False)
    cases = models.IntegerField(default=0,blank=False)
    recovered = models.IntegerField(default=0,blank=False)
    death = models.IntegerField(default=0,blank=False)


class Shop(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=30, blank=True)
    address = models.CharField(max_length=30, blank=False)
    type = models.CharField(max_length=30, blank=False)
    description = models.TextField(max_length=300, blank=True)
    limit = models.IntegerField(default=0,blank=False)


class Expedition(models.Model):
    userprofile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True, blank=False)
    expected = models.DateTimeField(auto_now=False, blank=False)
    status = models.CharField(max_length=30, blank=False)
