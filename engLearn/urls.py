from django.contrib.auth.decorators import login_required
from django.urls import path

from engLearn import views
from engLearn.views import WordsListView, WordsDetailView, profile

urlpatterns = [
    path('', WordsListView.as_view(), name='home'),
    path('accounts/profile/', profile, name='profile'),
    path('<slug:word_slug>/', WordsDetailView.as_view(), name='word_detail'),
    path('<slug:word_slug>/add_examples/', views.add_examples, name='add_examples'),
    path('<slug:word_slug>/change_image/', views.change_image, name='change_image'),
]
