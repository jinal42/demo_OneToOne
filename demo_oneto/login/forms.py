from .models import User,UserProfile
from  django import forms
from django.contrib.auth.forms import UserCreationForm

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','email','first_name','last_name','password1','password2')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['phone','gender','hobby','birth_date']