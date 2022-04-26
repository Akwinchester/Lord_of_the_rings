from django.urls import path
from .views import *

urlpatterns = [

    # path('',page_character_views, name='page_character'), #для представления домашней страницы функцией
    path('', Page_character.as_view(), name='page_character'),
    path('category/<int:cat_id>/',Page_character_category.as_view(), name="category"),
    path('personal/<int:id_character>/', personal_page_views, name='personal_page'),
    path('forma', addpage, name='Addpage'),

 ]