from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from .models import Profile

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Password'}))

class OTPForm(forms.Form):
    otp = forms.CharField(max_length=6,widget=forms.TextInput(attrs={'placeholder':'Enter OTP'}))

class ProfileForm(forms.ModelForm):
        class Meta:
            model = Profile
            fields = ['mobile_num','address','wesite','country']
            wedget = {
                'mobile_num':forms.TextInput(attrs={'placeholder':'Mobile Number'}),
                'address':forms.TextInput(attrs={'placeholder':'Address'}),
                'wesite':forms.TextInput(attrs={'placeholder':'Website'}),
                'country':forms.TextInput(attrs={'placeholder':'Country'})
            }