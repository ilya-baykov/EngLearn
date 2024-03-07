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

    # def get_queryset(self):
    #     return Words.objects.all()


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
        context['page_number'] = self.request.GET.get('page')
        return context


