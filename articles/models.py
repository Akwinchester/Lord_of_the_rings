import datetime
from django.urls import reverse
from django.db import models

class page_character(models.Model):
    name_character = models.CharField(max_length=30, verbose_name='имя' )
    text_character = models.TextField(verbose_name='текст статьи' )
    photo_character = models.ImageField(upload_to="photos/%Y/%m/%d/",blank=True, verbose_name='фото', default=None) #blank=True => поле может быть пустым
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name='категория')
    date_add_character = models.DateTimeField(auto_now_add=True,blank=True,verbose_name='дата добавления записи')
    def __str__(self):
        return self.name_character

class Category(models.Model):
    type_objects = models.CharField(max_length= 100, db_index=True)

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_id': self.pk})

    def __str__(self):
        return self.type_objects