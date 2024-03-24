from django.contrib.auth.models import User
from django.db import models


class MyWords(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='user')
    en_word = models.CharField(max_length=45, verbose_name='English word')
    ru_word = models.CharField(max_length=45, verbose_name='Translate to Russian')
    en_example = models.TextField(verbose_name="English Example")
    ru_example = models.TextField(verbose_name="Translate To Russian")
    slug = models.SlugField(unique=True)
    img = models.ImageField(upload_to='my_added_words/%Y%m%d/', blank=True)
    date_add = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date_add',)

    def get_absolute_url(self):
        return self.slug

    def __str__(self):
        return f'My added word: {self.en_word} - {self.ru_word}'


class MyWordExamples(models.Model):
    my_word = models.ForeignKey(MyWords, on_delete=models.CASCADE, related_name='my_word')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    en_example_user = models.CharField(max_length=150, blank=False, verbose_name='English Example')
    ru_example_user = models.CharField(max_length=150, blank=False, verbose_name="Translate to Russian")

    def __str__(self):
        return f'{self.user} - {self.en_example_user}'
