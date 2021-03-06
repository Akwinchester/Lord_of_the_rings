# Generated by Django 4.0.2 on 2022-02-25 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_rename_name_page_character_name_character_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page_character',
            name='age_character',
            field=models.IntegerField(default=None, verbose_name='возраст'),
        ),
        migrations.AlterField(
            model_name='page_character',
            name='artifacts_character',
            field=models.CharField(blank=True, default=None, max_length=100, verbose_name='артифакты'),
        ),
        migrations.AlterField(
            model_name='page_character',
            name='capabilities_character',
            field=models.CharField(blank=True, default=None, max_length=250, verbose_name='способности'),
        ),
        migrations.AlterField(
            model_name='page_character',
            name='children_character',
            field=models.CharField(blank=True, default=None, max_length=50, verbose_name='дети'),
        ),
        migrations.AlterField(
            model_name='page_character',
            name='date_add_character',
            field=models.DateTimeField(auto_now_add=True, verbose_name='дата добавления записи'),
        ),
        migrations.AlterField(
            model_name='page_character',
            name='name_character',
            field=models.CharField(max_length=30, verbose_name='имя'),
        ),
        migrations.AlterField(
            model_name='page_character',
            name='parents_character',
            field=models.CharField(blank=True, default=None, max_length=50, verbose_name='родители'),
        ),
        migrations.AlterField(
            model_name='page_character',
            name='photo_character',
            field=models.ImageField(blank=True, default=None, upload_to='photos/%Y/%m/%d/', verbose_name='фото'),
        ),
        migrations.AlterField(
            model_name='page_character',
            name='race_character',
            field=models.CharField(default=None, max_length=30, verbose_name='расса'),
        ),
        migrations.AlterField(
            model_name='page_character',
            name='text_character',
            field=models.TextField(verbose_name='текст статьи'),
        ),
    ]
