from django.shortcuts import render
from .models import Bundle, Task
from django.utils import timezone


def index(request):
    context = {'all_bundles_list': Bundle.objects.all()}

    data_from_site = request.POST
    if data_from_site:
        create_new_bundle_and_tasks(data_from_site.get('new_bundle_name'), data_from_site.getlist('list_of_tasks'))
    return render(request, 'main_page/index.html', context)


# Create your views here.
def test(request):
    my_dict = {"test": "test"}
    return render(request, 'main_page/test.html', context=my_dict)


def create_new_bundle_and_tasks(name_of_new_bundle, list_of_new_tasks):
    Bundle(name=name_of_new_bundle, created_date=timezone.now()).save()
    temp = Bundle.objects.filter(name=name_of_new_bundle)[0]
    for new_task in list_of_new_tasks:
        Task(name_of_bundle=temp, task_description=new_task).save()
