from django.shortcuts import render, HttpResponse, redirect
from .models import Words, WordExamples, WordImageUser
from .forms import WordExamplesForm, ChangeImageForm

app_name = 'engLearn_cart_edit'


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


def remove_current_example(request, example_id, word_slug):
    if request.method == 'POST':
        example = WordExamples.objects.get(id=example_id)
        print(example)
        example.delete()
    return redirect('word_detail', word_slug=word_slug)
