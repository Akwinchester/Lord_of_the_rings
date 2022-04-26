from django.urls import path
from .views import  *

urlpatterns = [
    path('register', RegisterUser.as_view(), name='register_page'),
    path('login', Login_user.as_view(), name="Login_user_page"),
    path('logout/', logout_view, name='logout'),
 ]