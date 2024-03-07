from django.urls import path
from . import views

urlpatterns = [
    path('', views.MyWordsListView.as_view(), name='my_added_words_list'),

]
