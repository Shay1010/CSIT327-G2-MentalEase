from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Student

# Sign-up form
class StudentSignUpForm(forms.Form):
    username = forms.CharField(max_length=100)
    full_name = forms.CharField(max_length=100)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

# Login form
class StudentLoginForm(forms.Form):
    email = forms.EmailField(label="Email")
    password = forms.CharField(widget=forms.PasswordInput)

#Profile form
class StudentProfileForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['full_name', 'year_program', 'profile_picture']
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control'}),
            'year_program': forms.TextInput(attrs={'class': 'form-control'}),
        }
