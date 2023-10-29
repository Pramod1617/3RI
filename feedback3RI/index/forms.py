from django import forms
from .models import visitor, user
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class Visitordetails(forms.ModelForm):
    class Meta:
        model = visitor
        fields = ('Name','Email','Phone_number','Message')

class SignUpFrom(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password1','password2']

class Feedback(forms.ModelForm):
    class Meta:
        model = user
        fields = ['Name','Email','Rating','Message']

