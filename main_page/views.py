from django.shortcuts import render


def index(request):
    my_dict = {"test": "test"}
    return render(request, 'main_page/index.html', context=my_dict)
# Create your views here.
