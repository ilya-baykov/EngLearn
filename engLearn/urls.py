from django.urls import path

from engLearn import views
from engLearn.views import WordsListView

urlpatterns = [
    path('', WordsListView.as_view(), name='home'),
    # path('<slug:word_slug>', WordsListView.as_view(), name='word_detail'),
    path('<slug:word_slug>', views.detail_view, name='word_detail'),
]
