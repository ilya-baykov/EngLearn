from django.contrib import admin
from .models import Words


@admin.register(Words)
class WordsAdmin(admin.ModelAdmin):
    list_display = ['id', 'slug', 'en_word', 'ru_word', 'img_link']
