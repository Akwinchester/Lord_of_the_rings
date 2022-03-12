# Generated by Django 4.0.2 on 2022-02-11 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='page_character',
            old_name='name',
            new_name='name_character',
        ),
        migrations.RenameField(
            model_name='page_character',
            old_name='race',
            new_name='race_character',
        ),
        migrations.RenameField(
            model_name='page_character',
            old_name='text',
            new_name='text_character',
        ),
        migrations.RemoveField(
            model_name='page_character',
            name='photo',
        ),
        migrations.AddField(
            model_name='page_character',
            name='photo_character',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='page_character',
            name='age_character',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='page_character',
            name='artifacts_character',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='page_character',
            name='capabilities_character',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AlterField(
            model_name='page_character',
            name='children_character',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='page_character',
            name='date_add_character',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='page_character',
            name='parents_character',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
