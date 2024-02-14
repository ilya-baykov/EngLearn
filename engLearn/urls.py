from django.urls import path

from engLearn import views
from engLearn.views import WordsListView, WordsDetailView

urlpatterns = [
    path('', WordsListView.as_view(), name='home'),
    path('<slug:word_slug>/', WordsDetailView.as_view(), name='word_detail'),
]
