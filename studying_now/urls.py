from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('', login_required(views.StudyingNowListView.as_view()), name='studying_now'),
]
