from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.http import HttpResponse
from .models import page_character, Category
from django.views.generic import ListView, CreateView
from django.contrib.auth.views import LoginView
from .forms import Add_post_form, Add_user_form
from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from  django.contrib.auth import logout
from django.urls import reverse_lazy
# from django.core.paginator import Paginator #надо использовать для пагинации в представлениях-функциях

class Page_character(ListView):
    paginate_by = 3
    model = page_character
    template_name = "articles/page_character.html"
    context_object_name = 'posts' # по умолчанию используется object_list
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cats'] = Category.objects.all()
        return context
#конец представления домашней страницы на основе класса

class Page_character_category(ListView):
    paginate_by = 3
    model = page_character
    template_name = "articles/page_character.html"
    context_object_name = 'posts'  # по умолчанию используется object_list
    def get_queryset(self):
        print(self.kwargs['cat_id'])
        return page_character.objects.filter(cat_id=self.kwargs['cat_id'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cats'] = Category.objects.all()
        return context




def personal_page_views(request, id_character):
    #post = get_object_or_404(page_character, pk = id_charcter)
    character = page_character.objects.get(id = id_character)
    context = {
        'character': character
    }
    return render(request, template_name='articles/personal_page.html', context=context)

# форма добавления поста
def addpage(request):
    if request.method == 'POST':
        form = Add_post_form(request.POST, request.FILES)
        if form.is_valid():
            try:
                page_character.objects.create(**form.cleaned_data)
                return redirect(reverse('page_character'))
            except:
                form.add_error(None, 'Ошибка добавления поста')
    else:
        form = Add_post_form()
    context = {
        'form': form
    }
    return render(request, template_name="articles/addpage.html", context=context)

# класс-представление Регистрации пользователя
class RegisterUser(CreateView):
    # form_class = UserCreationForm
    form_class = Add_user_form
    template_name = 'articles/register.html'
    success_url = reverse_lazy('page_character')

class Login_user(LoginView):
    form_class = AuthenticationForm
    template_name = "articles/login.html"
    def get_success_url(self):
        return reverse_lazy('page_character')

def logout_view(request):
    logout(request)
    print("Нажал кнопку выйти")
    return redirect('Login_user_page')