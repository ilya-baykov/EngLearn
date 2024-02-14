from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Words

app_name = 'engLearn'


class WordsListView(ListView):
    model = Words
    template_name = 'engLearn/base.html'
    context_object_name = 'words'
    extra_context = {'title': 'EngLearn'}

    # def get_context_data(self, **kwargs):
    #     contex = super().get_context_data(**kwargs)
    #     contex['words'] = Words.objects.all()
    #     return contex

    def get_queryset(self):
        return Words.objects.all()
