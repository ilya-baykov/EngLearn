from django.shortcuts import render
# Create your views here.
from django.views.generic import ListView
from . import models


# Create your models here.


class StudyingNowListView(ListView):
    model = models.StudyingNowModel
    template_name = 'studying_now/rofl.html'
