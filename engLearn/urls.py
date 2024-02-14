from django.urls import path

from engLearn import views

urlpatterns = [
    path('', views.index, name='index'),
]
