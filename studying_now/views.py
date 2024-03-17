from django.db.models import Prefetch
from django.views.generic import ListView
from engLearn.models import Words, WordExamples, WordImageUser
from . import models
from .models import StudyingNowModel
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages


class StudyingNowListView(ListView):
    model = models.StudyingNowModel
    template_name = 'studying_now/studying_now_list.html'
    context_object_name = 'studying_now_objects'

    def get_queryset(self):
        studying_now_objects = StudyingNowModel.objects.filter(user=self.request.user).order_by(
            '-date_added').select_related('word')

        for obj in studying_now_objects:
            obj.word.wordexamples_set = WordExamples.objects.filter(word=obj.word, user=self.request.user)
            obj.word.user_images = WordImageUser.objects.filter(word=obj.word, user=self.request.user).first()

        return studying_now_objects

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Studying now'
        return context


def add_to_studying_now(request, word_slug):
    if request.method == 'POST':

        word = Words.objects.get(slug=word_slug)
        user_studying_now_words = StudyingNowModel.objects.filter(user=request.user)
        if user_studying_now_words.filter(word=word):
            messages.warning(request, f'Слово "{word}" уже сохранено для изучения.')
        else:
            StudyingNowModel.objects.get_or_create(user=request.user, word=word)
            messages.success(request, f'Слово "{word}" успешно добавлено в список изучения.')

    page_number = request.POST.get('page')
    uri = reverse('word_detail', args=(word_slug,)) + f'?page={page_number}'
    return HttpResponseRedirect(uri)


def remove_from_studying_now(request, word_slug):
    if request.method == 'POST':
        word = Words.objects.get(slug=word_slug)
        studying_now_model = StudyingNowModel.objects.get(user=request.user, word=word)
        studying_now_model.delete()
        uri = reverse('studying_now')
        return HttpResponseRedirect(uri)
