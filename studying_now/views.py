from django.contrib.auth.models import User
from django.shortcuts import render
# Create your views here.
from django.views.generic import ListView

from engLearn.models import Words
from . import models
from itertools import chain
from operator import attrgetter

from .models import StudyingNowModel


# Create your models here.


class StudyingNowListView(ListView):
    model = models.StudyingNowModel
    template_name = 'studying_now/rofl.html'
    context_object_name = 'save_words'

    def get_queryset(self):
        studying_now_objects = StudyingNowModel.objects.filter(user=self.request.user)
        studying_words = Words.objects.filter(studying_now_word__in=studying_now_objects).order_by(
            '-studying_now_word__date_added')

        return studying_words
