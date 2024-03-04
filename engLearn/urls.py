from django.contrib.auth.decorators import login_required
from django.urls import path

from engLearn import views
from engLearn.views import WordsListView, WordsDetailView, profile

urlpatterns = [
    path('', WordsListView.as_view(), name='home'),
    path('accounts/profile/', profile, name='profile'),
    path('<slug:word_slug>/', WordsDetailView.as_view(), name='word_detail'),
    path('add_to_studying/<slug:word_slug>/', views.add_to_studying_now, name='add_to_studying'),
]
