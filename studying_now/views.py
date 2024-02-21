from django.contrib.auth.models import User
from django.shortcuts import render
# Create your views here.
from django.views.generic import ListView
from . import models
from itertools import chain


# Create your models here.


class StudyingNowListView(ListView):
    model = models.StudyingNowModel
    template_name = 'studying_now/rofl.html'
    context_object_name = 'save_words'

    def get_queryset(self):
        studying_now_objects = models.StudyingNowModel.objects.filter(user=self.request.user)
        studying_words = chain.from_iterable([user.studying_now_word.all() for user in studying_now_objects])
        return studying_words
