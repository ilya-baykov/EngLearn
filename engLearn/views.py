from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Words

app_name = 'engLearn'


class WordsListView(ListView):
    model = Words
    template_name = 'engLearn/home_page.html'
    context_object_name = 'words'
    extra_context = {'title': 'EngLearn'}
    paginate_by = 10

    def get_queryset(self):
        return Words.objects.all()


def detail_view(request, word_slug):
    word = Words.objects.get(slug=word_slug)
    print(word)
    return render(request, template_name='engLearn/word_detail.html', context={'word': word})

# class WordsDetailView(DetailView):
#     model = Words
#     template_name = 'engLearn/word_detail.html'
