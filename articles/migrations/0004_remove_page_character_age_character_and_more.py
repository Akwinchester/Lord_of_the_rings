# Generated by Django 4.0.2 on 2022-02-25 11:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_alter_page_character_age_character_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='page_character',
            name='age_character',
        ),
        migrations.RemoveField(
            model_name='page_character',
            name='artifacts_character',
        ),
        migrations.RemoveField(
            model_name='page_character',
            name='capabilities_character',
        ),
        migrations.RemoveField(
            model_name='page_character',
            name='children_character',
        ),
        migrations.RemoveField(
            model_name='page_character',
            name='parents_character',
        ),
        migrations.RemoveField(
            model_name='page_character',
            name='race_character',
        ),
    ]
