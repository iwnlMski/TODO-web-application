from django.shortcuts import render


def index(request):
    my_dict = {"test": "test"}
    render(request, 'templates/index.html', context=my_dict)
# Create your views here.
