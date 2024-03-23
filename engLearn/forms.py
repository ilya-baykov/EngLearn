from django import forms




class ChangeImageForm(forms.Form):
    image = forms.ImageField()
