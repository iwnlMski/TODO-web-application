from django.shortcuts import render
from .models import Bundle, Task


def index(request):
    all_bundles_list = Bundle.objects.all()
    context = {'all_bundles_list': all_bundles_list}
    my_dict = {"test": "test"}
    return render(request, 'main_page/index.html', context)


# Create your views here.
def test(request):
    my_dict = {"test": "test"}
    return render(request, 'main_page/test.html', context=my_dict)
