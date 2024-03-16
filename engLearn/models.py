from django.contrib.auth.models import User
from django.db import models


class Words(models.Model):
    en_word = models.CharField(max_length=45)
    ru_word = models.CharField(max_length=45)
    en_example = models.TextField()
    ru_example = models.TextField()
    slug = models.SlugField(unique=True)
    img_link = models.URLField(blank=True)
    in_study = models.ManyToManyField(User, related_name='in_study_words', through="studying_now.StudyingNowModel",
                                      through_fields=('word', 'user'))
    user_example = models.ManyToManyField(User, related_name='user_example', through="engLearn.WordExamples",
                                          through_fields=('word', 'user'))

    picurl = models.TextField(blank=True)
    picau = models.CharField(max_length=60)
    gap = models.CharField(max_length=5, default=None)

    def get_absolute_url(self):
        return self.slug

    def __str__(self):
        return f'{self.en_word} - {self.ru_word}'


class WordExamples(models.Model):
    word = models.ForeignKey(Words, on_delete=models.CASCADE, related_name='word')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    en_example_user = models.TextField()
    ru_example_user = models.TextField()

    def __str__(self):
        return f'{self.user} - {self.en_example_user}'
from django.contrib.auth.models import User
