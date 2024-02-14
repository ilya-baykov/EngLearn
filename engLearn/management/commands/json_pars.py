import json
from django.core.management.base import BaseCommand
from engLearn.models import Words
import re


# from engLearn.models import Words


class Command(BaseCommand):
    help = 'Load words from JSON file to the database'

    def handle(self, *args, **options):
        with open('/home/ilyabaykov/PycharmProjects/EngLearn/words.json') as f:
            templates = json.load(f)
        del templates[0]

        slug_used = []
        for word in range(5000):
            id_word = templates[word]['id']
            eng = re.sub(r'\d', '', templates[word]['eng'])
            rus = templates[word]['rus']
            enex = templates[word]['enex']
            ruex = templates[word]['ruex']
            picurl = templates[word]['picurl']
            picau = templates[word]['picau']
            gap = templates[word]['gap']
            slug = re.sub(r'\d', '', templates[word]['eng'].split()[0])
            slug_used.append(slug)
            slug = slug + str(slug_used.count(slug) + 1)
            url_img = f"https://britlex.ru/images/{str(templates[word]['eng'].split()[0])}.jpg"
            print(id_word, slug)
            Words.objects.create(en_word=eng, ru_word=rus, en_example=enex, ru_example=ruex, picurl=picurl, picau=picau,
                                 gap=gap, slug=slug, img_link=url_img)
