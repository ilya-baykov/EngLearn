from django.shortcuts import render, HttpResponse, redirect
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


def remove_current_example(request, example_id, word_slug):
    if request.method == 'POST':
        example = WordExamples.objects.get(id=example_id)
        print(example)
        example.delete()
    return redirect('word_detail', word_slug=word_slug)
