from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from studying_now.models import StudyingNowModel
from .models import Words

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
        return Words.objects.all().order_by('id')


class WordsDetailView(DetailView):
    model = Words
    template_name = 'engLearn/word_detail.html'
    context_object_name = 'word'
    slug_url_kwarg = 'word_slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            print(self.request.user)
            user_studying_words = StudyingNowModel.objects.filter(user=self.request.user)
            print(user_studying_words)
            current_word = Words.objects.get(slug=self.kwargs['word_slug'])
            print(current_word)
            context['in_list'] = user_studying_words.filter(word=current_word)
            print(context['in_list'])
        context['page_number'] = self.request.GET.get('page')
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.order_by('id')
