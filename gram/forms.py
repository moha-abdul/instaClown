from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile,Image, Comment

class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('profile_photo', 'profile_bio')

class ImageForm(forms.ModelForm):
	class Meta:
		model = Image
		exclude = ['user','time_created','time_updated','date_uploaded','profile','image_name',]

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['user', 'image_name']
        fields = ['comment']