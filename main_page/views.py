from django.shortcuts import render
from .models import Bundle, Task
from django.utils import timezone
from django.db import IntegrityError
from .main_page_func import *


def index(request):
    context = {}
    request_data = request.POST

    if request_data.get('bundle_to_delete'):
        delete_bundle_and_tasks(request_data.get('bundle_to_delete'))

    if request_data.get('new_bundle_name'):
        try:
            create_new_bundle_and_tasks(request_data.get('new_bundle_name'), request_data.getlist('list_of_tasks'))
        except IntegrityError:
            context['IntegrityError'] = 'Couldn\'t create bundle. Bundle with that name already exists '

    context['all_bundles_list'] = Bundle.objects.all()
    context['data_json'] = len(Bundle.objects.all())
    return render(request, 'main_page/index.html', context)


def test(request):
    context = {}
    return render(request, 'main_page/createlist.html', context)


def show_tasks(request):
    request_data = request.POST
    print(request_data)
    if request_data.get('bundle_choice'):
        bundle_name = request_data.get('bundle_choice')
        context = {'bundle': get_bundle_by_name(bundle_name).task_set.all(),
                   'progress': calculate_bundle_progress(bundle_name)}

    elif request_data.get('task_move_right') or request_data.get('task_move_left'):
        context = change_task_status_and_return_context(request_data)

    elif request_data.get('task_description') or request_data.get('task_description') == '':
        bundle = add_description_to_task_and_return_bundle(request_data.get('task_to_change'),
                                                           request_data.get('task_description'))
        context = {'bundle': bundle.task_set.all(),
                   'progress': calculate_bundle_progress(bundle.name)}
    else:
        context = {}
    return render(request, 'main_page/listtasks.html', context)


