from django.contrib.auth.decorators import login_required
from django.urls import path
from . import views

urlpatterns = [
    path('', login_required(views.MyWordsListView.as_view()), name='my_added_words_list'),
    path('add_word/', views.add_to_my_added_word, name='add_to_my_added_word'),
    path('remove_word/<slug:word_slug>/', views.remove_from_my_added_word, name='remove_from_my_added_word'),
    path('add_examples/<slug:word_slug>/', views.AddExampleView.as_view(), name='add_examples_my_added_word'),

]
