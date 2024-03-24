from django.contrib.auth.decorators import login_required
from django.urls import path

from engLearn import views, views_cart_edit
from engLearn.views import WordsListView, WordsDetailView, profile

urlpatterns = [
    path('', WordsListView.as_view(), name='home'),
    path('accounts/profile/', profile, name='profile'),
    path('<slug:word_slug>/', WordsDetailView.as_view(), name='word_detail'),
    path('<str:source>/<slug:word_slug>/add_examples/', views_cart_edit.AddWordExample.as_view(), name='add_examples'),
    path('<slug:word_slug>/change_image/', views_cart_edit.EditImageWordExample.as_view(), name='change_image'),
    path('<int:example_id>/<slug:word_slug>/remove_example/', views_cart_edit.DeleteWordExample.as_view(),
         name='remove_example'),
]
