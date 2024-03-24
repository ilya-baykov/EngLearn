from django.contrib import admin
from .models import MyWords


@admin.register(MyWords)
class MyWordAdmin(admin.ModelAdmin):
    list_display = ['user']
    # list_display = ['id', 'slug', 'en_word', 'ru_word', 'img', 'date_add']
    prepopulated_fields = {"slug": ("en_word",)}
