from django import forms
from django.contrib.auth.forms import AuthenticationForm

class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(label='ユーザー名', max_length=100)
    password = forms.CharField(label='パスワード', widget=forms.PasswordInput)

class NoteForm(forms.Form):
    title = forms.CharField(max_length=200, required=True)
    body = forms.CharField(widget=forms.Textarea, required=True)