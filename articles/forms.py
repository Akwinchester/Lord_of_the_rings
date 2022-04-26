from django import forms
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

