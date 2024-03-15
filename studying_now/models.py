from django.contrib.auth.models import User
from django.db import models
from django.db.models import ForeignKey

from engLearn.models import Words


class StudyingNowModel(models.Model):
    user = ForeignKey(User, on_delete=models.CASCADE)
    word = ForeignKey(Words, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.id}-{self.user}-{self.word}"

    # class StudyingNowModel(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     studying_now_word = models.ManyToManyField(Words, related_name='studying_now_word', blank=True)
#     date_added = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return f'{self.user.username} - {len(self.studying_now_word.all())}'
#
