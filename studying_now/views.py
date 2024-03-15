from django.views.generic import ListView
from engLearn.models import Words
from . import models
from .models import StudyingNowModel
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages


# Create your models here.


class StudyingNowListView(ListView):
    model = models.StudyingNowModel
    template_name = 'studying_now/studying_now_list.html'
    context_object_name = 'save_words'

    def get_queryset(self):
        studying_now_objects = StudyingNowModel.objects.filter(user=self.request.user)
        studying_now_sorted = studying_now_objects.order_by('-date_added')
        studying_words = Words.objects.filter(studying_now_word__in=studying_now_sorted)
        print(studying_words)
        return studying_words

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Studying now'
        return context


def add_to_studying_now(request, word_slug):
    if request.method == 'POST':
        word = Words.objects.get(slug=word_slug)
        studying_now = StudyingNowModel.objects.get(user=request.user)
        if word in studying_now.studying_now_word.all():
            messages.warning(request, f'Слово "{word}" уже сохранено для изучения.')
        else:
            studying_now.studying_now_word.add(word)
            messages.success(request, f'Слово "{word}" успешно добавлено в список изучения.')
    page_number = request.POST.get('page')
    uri = reverse('word_detail', args=(word_slug,)) + f'?page={page_number}'
    return HttpResponseRedirect(uri)


def remove_from_studying_now(request, word_slug):
    if request.method == 'POST':
        word = Words.objects.get(slug=word_slug)
        studying_now = StudyingNowModel.objects.get(user=request.user)
        studying_now.studying_now_word.remove(word)
        uri = reverse('studying_now')
        return HttpResponseRedirect(uri)
