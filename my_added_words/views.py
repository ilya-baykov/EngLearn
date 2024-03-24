from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.utils.text import slugify
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from . import models
from .forms import MyWordForm
from .models import MyWordExamples, MyWords


class MyWordsListView(ListView):
    model = models.MyWords
    template_name = 'my_added_words/my_added_words_list.html'
    paginate_by = 10
    context_object_name = 'my_added_words'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "My Added Words"
        context['form'] = MyWordForm()
        return context

    def get_queryset(self):
        return models.MyWords.objects.filter(user=self.request.user)


class AddMyWord(CreateView):
    model = MyWords
    fields = ["en_word", "ru_word", "en_example", "ru_example", "img"]
    template_name = 'my_added_words/add_my_word_page.html'
    success_url = reverse_lazy('my_added_words_list')
    extra_context = {
        'title': "Добавление слова"
    }

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.slug = slugify(form.instance.en_word)
        return super().form_valid(form)


class RemoveMyWord(DeleteView):
    model = MyWords
    success_url = reverse_lazy('my_added_words_list')

    def get_object(self, queryset=None):
        return models.MyWords.objects.get(slug=self.kwargs['word_slug'])


class AddExampleView(CreateView):
    model = MyWordExamples
    template_name = "engLearn/add_examples.html"
    fields = ["en_example_user", "ru_example_user"]

    def form_valid(self, form):
        word = models.MyWords.objects.get(slug=self.kwargs['word_slug'])
        form.instance.my_word = word
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('my_added_words_list')
