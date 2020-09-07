from .models import *
from django.db.models import Q
from datetime import datetime, timedelta, time
from django.utils import timezone
from django.db.models import Count

def get_profile(user_id):
    profile = Profile.objects.get(user_id=user_id)
    return profile


def get_profile_id(user_id):
    profile = Profile.objects.get(user_id=user_id)
    return profile.id


def get_control(profile_id):
    control = Control.objects.filter(userprofile_id=profile_id).order_by('-date')
    return control


def deletemon(monitoring_id):
    Control.objects.filter(id=monitoring_id).delete()


def get_calls(profile_id):
    calls = Call.objects.filter(userprofile_id=profile_id).order_by('-date')
    return calls


def get_call(call_id):
    call = Call.objects.get(id=call_id)
    return call


def get_statisctics():
    return Statistics.objects.all()


def get_all_statistic():
    return Statistics.objects.get(id=2)


def isShop(user_id):
    try:
        Shop.objects.get(user_id=user_id)
        return True
    except:
        return False


def get_shops():
    return Shop.objects.all()


def get_health(user_id):
    return Control.objects.filter(userprofile_id=user_id)


def get_expedition(user_id):
    return Expedition.objects.filter(userprofile_id=user_id)


def get_expedition_for(shop_id, user_id):
    return Expedition.objects.get(shop_id=shop_id, userprofile_id=user_id)


def check_duplications(user_id, shop_id):
    exp = Expedition.objects.filter(userprofile_id=user_id, shop_id=shop_id)
    exp.delete()


def get_shop_id(user_id):
    return Shop.objects.get(user_id=user_id).id


def get_for_shop(user_id):
    shop = Shop.objects.get(user_id = user_id)
    return Expedition.objects.filter(shop_id=shop.id)
