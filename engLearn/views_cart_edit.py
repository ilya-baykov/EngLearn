from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.urls import reverse_lazy
from .models import Words, WordExamples, WordImageUser
from django.views.generic.edit import CreateView, UpdateView, DeleteView

app_name = 'engLearn_cart_edit'


class AddWordExample(CreateView):
    model = WordExamples
    fields = ["en_example_user", "ru_example_user"]
    template_name = 'engLearn/add_examples.html'

    def form_valid(self, form):
        word_slug = self.kwargs['word_slug']
        word = Words.objects.get(slug=word_slug)
        form.instance.word = word
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        word_slug = self.kwargs['word_slug']
        return reverse_lazy('word_detail', kwargs={'word_slug': word_slug})


class EditImageWordExample(UpdateView):
    model = WordImageUser
    fields = ["image"]
    template_name = 'engLearn/change_image.html'

    def get_object(self, queryset=None):
        word = Words.objects.get(slug=self.kwargs['word_slug'])
        word_img_obj, created = WordImageUser.objects.get_or_create(word=word, user=self.request.user)
        return word_img_obj

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.word = Words.objects.get(slug=self.kwargs['word_slug'])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('word_detail', kwargs={'word_slug': self.kwargs['word_slug']})


def remove_current_example(request, example_id, word_slug):
    if request.method == 'POST':
        example = WordExamples.objects.get(id=example_id)
        print(example)
        example.delete()
    return redirect('word_detail', word_slug=word_slug)