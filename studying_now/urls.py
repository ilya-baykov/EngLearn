from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.StudyingNowListView.as_view(), name='studying_now'),
]
