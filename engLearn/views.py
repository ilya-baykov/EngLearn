from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from studying_now.models import StudyingNowModel
from .models import Words
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages

app_name = 'engLearn'


@login_required
def profile(request):
    return render(request, 'engLearn/profile.html')


class WordsListView(ListView):
    model = Words
    template_name = 'engLearn/home_page.html'
    context_object_name = 'words'
    extra_context = {'title': 'EngLearn'}
    paginate_by = 10

    def get_queryset(self):
        return Words.objects.all()


class WordsDetailView(DetailView):
    model = Words
    template_name = 'engLearn/word_detail.html'
    context_object_name = 'word'
    slug_url_kwarg = 'word_slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Word Details'
        word = self.get_object()
        studying_now, created = StudyingNowModel.objects.get_or_create(user=self.request.user)
        in_list = word in studying_now.studying_now_word.all()
        context['in_list'] = in_list
        return context


def add_to_studying_now(request, word_slug):
    if request.method == 'POST':
        word = Words.objects.get(slug=word_slug)
        studying_now = StudyingNowModel.objects.get(user=request.user)
        print(studying_now)
        if word in studying_now.studying_now_word.all():
            messages.warning(request, f'Слово "{word}" уже сохранено для изучения.')
            in_list = True
        else:
            studying_now.studying_now_word.add(word)
            messages.success(request, f'Слово "{word}" успешно добавлено в список изучения.')
            in_list = False
        uri = reverse('word_detail', args=(word_slug,))
        return HttpResponseRedirect(uri, messages)
