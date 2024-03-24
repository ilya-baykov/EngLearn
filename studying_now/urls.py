from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', login_required(views.StudyingNowListView.as_view()), name='studying_now'),
    path('<slug:word_slug>/', views.AddStudyingNowView.as_view(), name='add_to_studying'),
    path('remove_word/<slug:word_slug>/', views.remove_from_studying_now, name='remove_from_studying'),
]
