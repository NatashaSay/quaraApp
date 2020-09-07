from django import forms
from django.contrib.auth.models import User
from quaraDB.models import User, Profile, Control, Call
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.forms import UserCreationForm


class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ('image', 'firstname', 'lastname', 'city', 'age', 'bio', 'birthdate', 'district', 'address')


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['image', 'firstname', 'lastname', 'city', 'age', 'bio', 'birthdate', 'district', 'address']


class ControlForm(forms.ModelForm):

    class Meta:
        model = Control
        fields = ['temperature', 'cough', 'headache', 'comment']


class CallForm(forms.ModelForm):

    class Meta:
        model = Call
        fields = ['reason', 'urgently' ,'comment']
