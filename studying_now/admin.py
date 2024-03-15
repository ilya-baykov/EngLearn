from django.contrib import admin
from . import models


@admin.register(models.StudyingNowModel)
class StudyingNowAdmin(admin.ModelAdmin):
    list_display = ['word', 'user', 'date_added']
