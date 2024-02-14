from django.urls import path

from engLearn import views
from engLearn.views import WordsListView

urlpatterns = [
    path('', WordsListView.as_view(), name='home'),
]
