from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from studying_now.models import StudyingNowModel
from .models import Words, WordExamples, WordImageUser
from .forms import WordExamplesForm, ChangeImageForm

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
            user_studying_words = StudyingNowModel.objects.filter(user=self.request.user)
            current_word = Words.objects.get(slug=self.kwargs['word_slug'])
            context['in_list'] = user_studying_words.filter(word=current_word)
            context['user_examples'] = WordExamples.objects.filter(word=current_word, user=self.request.user)
            print(context['user_examples'])
        context['page_number'] = self.request.GET.get('page')
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.order_by('id')


def add_examples(request, word_slug):
    word = Words.objects.get(slug=word_slug)
    if request.method == 'POST':
        form = WordExamplesForm(request.POST)
        if form.is_valid():
            en_example_user = form.cleaned_data["en_example_user"]
            ru_example_user = form.cleaned_data["ru_example_user"]
            WordExamples.objects.create(user=request.user, word=word,
                                        en_example_user=en_example_user,
                                        ru_example_user=ru_example_user)
            return redirect('word_detail', word_slug=word.slug)
    else:
        form = WordExamplesForm()
        return render(request, 'engLearn/add_examples.html', {'word': word, 'form': form})


def change_image(request, word_slug):
    word = Words.objects.get(slug=word_slug)
    if request.method == 'POST':
        form = ChangeImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            obj, created = WordImageUser.objects.get_or_create(word=word, user=request.user)
            obj.image = image
            obj.save()
            return redirect('word_detail', word_slug=word.slug)
    else:
        form = ChangeImageForm()
    return render(request, 'engLearn/change_image.html', {'word': word, 'form': form})
