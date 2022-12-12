from django import forms

class LoginForm(forms.Form):
    email=forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Type Your Email Id','type': 'email'}),label='Email Id',required=True)
    password=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Type Your Password'}),label='Password',max_length=15,min_length=4,required=True)


