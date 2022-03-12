from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *
#форма не связанная с моделью
# class Add_post_form(forms.Form):
#     name_character = forms.CharField(max_length= 50, label="Имя")
#     text_character = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}), label='Текст')
#     photo_character = forms.ImageField()

#фрма связанная с моделью
class Add_post_form(forms.ModelForm):
    class Meta:
        model = page_character
        fields = ['name_character', 'text_character', 'photo_character', 'cat']

class Add_user_form(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input'}))