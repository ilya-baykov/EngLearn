from django.contrib.auth.models import User
from django.shortcuts import render
# Create your views here.
from django.views.generic import ListView
from . import models


# Create your models here.


class StudyingNowListView(ListView):
    model = models.StudyingNowModel
    template_name = 'studying_now/rofl.html'
    context_object_name = 'save_words'

    def get_queryset(self):
        return models.StudyingNowModel.objects.filter(user=self.request.user)
