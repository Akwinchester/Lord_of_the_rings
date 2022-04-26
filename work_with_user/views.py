from django.shortcuts import render
from .forms import Add_user_form
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse_lazy
from django.shortcuts import redirect



class RegisterUser(CreateView):
    # form_class = UserCreationForm
    form_class = Add_user_form
    template_name = 'work_with_user/register.html'
    success_url = reverse_lazy('page_character')

class Login_user(LoginView):
    form_class = AuthenticationForm
    template_name = "work_with_user/login.html"
    def get_success_url(self):
        return reverse_lazy('page_character')

def logout_view(request):
    logout(request)
    print("Нажал кнопку выйти")
    return redirect('Login_user_page')