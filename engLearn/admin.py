from django.contrib import admin
from .models import Words


# Register your models here.


@admin.register(Words)
class WordsAdmin(admin.ModelAdmin):
    list_display = ['id', 'slug', 'en_word', 'ru_word']

