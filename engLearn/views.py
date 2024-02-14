from django.shortcuts import render

app_name = 'engLearn'


def index(request):
    print("Вызов главной страницы")
    return render(request, "engLearn/base.html")
