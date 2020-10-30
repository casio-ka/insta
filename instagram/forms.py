from django import forms
from .models import Image, Profile, Comments
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user','following']

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['likes', 'name', 'profile', 'comments']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        exclude = ['image', 'user']