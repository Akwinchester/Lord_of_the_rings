from django.urls import path
from .views import *

urlpatterns = [

    # path('',page_character_views, name='page_character'), #для представления домашней страницы функцией
    path('', Page_character.as_view(), name='page_character'),
    path('category/<int:cat_id>/',Page_character_category.as_view(), name="category"),
    path('personal/<int:id_character>/', personal_page_views, name='personal_page'),
    path('forma', addpage, name='Addpage'),
    path('register', RegisterUser.as_view(), name='register_page'),
    path('login', Login_user.as_view(), name="Login_user_page"),
    path('logout/', logout_view, name='logout'),
 ]