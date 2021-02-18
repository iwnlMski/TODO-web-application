from django.shortcuts import render
from .models import Bundle, Task
from django.utils import timezone
from django.db import IntegrityError


def index(request):
    context = {}
    data_from_site = request.POST
    print(data_from_site)

    if data_from_site.get('bundle_to_delete'):
        delete_bundle_and_tasks(data_from_site.get('bundle_to_delete'))

    if data_from_site and data_from_site.get('new_bundle_name'):
        try:
            create_new_bundle_and_tasks(data_from_site.get('new_bundle_name'), data_from_site.getlist('list_of_tasks'))
        except IntegrityError:
            context['IntegrityError'] = 'Couldn\'t create bundle. Bundle with that name already exists '

    context['all_bundles_list'] = Bundle.objects.all()
    context['data_json'] = len(Bundle.objects.all())
    return render(request, 'main_page/index.html', context)


# Create your views here.
def test(request):
    context = {}
    return render(request, 'main_page/createlist.html', context)


def show_tasks(request):
    data_from_site = request.POST
    if data_from_site.get('bundle_choice'):
        bundle_name = data_from_site.get('bundle_choice')
        context = {'bundle': get_bundle_by_name(bundle_name).task_set.all(),
                   'progress': calculate_bundle_progress(bundle_name)}

    elif data_from_site.get('task_move_right') or data_from_site.get('task_move_left'):
        context = change_task_status_and_return_context(data_from_site)

    else:
        context = {}
    return render(request, 'main_page/listtasks.html', context)


def remove_empty_tasks(list_of_tasks):
    for i in range(list_of_tasks.count('')):
        list_of_tasks.remove('')
    return list_of_tasks


def create_new_bundle_and_tasks(name_of_new_bundle, list_of_new_tasks):
    Bundle(name=name_of_new_bundle, created_date=timezone.now()).save()
    temp = Bundle.objects.filter(name=name_of_new_bundle)[0]

    list_of_new_tasks = remove_empty_tasks(list_of_new_tasks)
    for new_task in list_of_new_tasks:
        Task(name_of_bundle=temp, task_description=new_task).save()


def get_bundle_by_name(bundle_name):
    return Bundle.objects.filter(name=bundle_name)[0]


def delete_bundle_and_tasks(bundle_name):
    bundle = Bundle.objects.filter(name=bundle_name)[0]
    for task in bundle.task_set.all():
        task.delete()
    bundle.delete()


def calculate_bundle_progress(bundle_name):
    bundle = Bundle.objects.filter(name=bundle_name)[0]
    return len(bundle.task_set.all().filter(current_status=3)) / len(bundle.task_set.all()) * 100


def change_task_status_and_return_context(data):
    task_description = data.get('task_move_right') if data.get('task_move_right') else data.get('task_move_left')
    task = Task.objects.filter(task_description=task_description)[0]
    bundle_name = task.name_of_bundle
    task.update_status(1 if data.get('task_move_right') else -1)
    context = {'bundle': get_bundle_by_name(bundle_name).task_set.all(),
               'progress': calculate_bundle_progress(bundle_name)}
    return context
