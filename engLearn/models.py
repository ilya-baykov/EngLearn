from django.db import models


# Create your models here.


class Words(models.Model):
    en_word = models.CharField(max_length=45)
    ru_word = models.CharField(max_length=45)
    en_example = models.TextField()
    ru_example = models.TextField()
    slug = models.SlugField(unique=True)

    def __str__(self):
        return f'{self.en_word} - {self.ru_word}'
