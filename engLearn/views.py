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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_images = WordImageUser.objects.filter(user=self.request.user).values('word__id', 'image')
        user_images_dict = {image['word__id']: image['image'] for image in user_images}
        context['user_images_dict'] = user_images_dict
        return context


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

            if WordImageUser.objects.filter(word=current_word, user=self.request.user):
                context['user_img'] = WordImageUser.objects.get(word=current_word, user=self.request.user).image.url
                print(context['user_img'])
            else:
                context['user_img'] = None
        context['page_number'] = self.request.GET.get('page')
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.order_by('id')




