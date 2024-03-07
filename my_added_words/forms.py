from django import forms


class MyWordForm(forms.Form):
    en_word = forms.CharField(label="Слово на английском языке", max_length=45)
    ru_word = forms.CharField(label="Перевод слова на русский язык", max_length=45)
    en_example = forms.CharField(label="Пример использования слова ( на английском )", widget=forms.Textarea,
                                 max_length=120)
    ru_example = forms.CharField(label="Перевод примера использования", widget=forms.Textarea, max_length=120)
    img = forms.ImageField(required=False)
