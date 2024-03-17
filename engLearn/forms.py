from django import forms


class WordExamplesForm(forms.Form):
    en_example_user = forms.CharField(label="Enter a usage example", max_length=150)
    ru_example_user = forms.CharField(label="Введите перевод примера", max_length=150)
