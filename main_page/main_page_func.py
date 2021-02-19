from .models import Bundle, Task
from django.utils import timezone


def remove_empty_tasks(list_of_tasks):
    for i in range(list_of_tasks.count('')):
        list_of_tasks.remove('')
    return list_of_tasks


def create_new_bundle_and_tasks(name_of_new_bundle, list_of_new_tasks):
    bundle = Bundle(name=name_of_new_bundle, created_date=timezone.now())
    bundle.save()

    list_of_new_tasks = remove_empty_tasks(list_of_new_tasks)
    for new_task in list_of_new_tasks:
        Task(parent_bundle=bundle, task_title=new_task).save()


def get_bundle_by_name(bundle_name):
    return Bundle.objects.filter(name=bundle_name)[0]


def get_task_by_name(task_name):
    return Task.objects.filter(task_title=task_name)[0]


def delete_bundle_and_tasks(bundle_name):
    bundle = get_bundle_by_name(bundle_name)
    tasks_list = bundle.task_set.all()
    for task in tasks_list:
        task.delete()
    bundle.delete()


def calculate_bundle_progress(bundle_name):
    bundle = get_bundle_by_name(bundle_name)
    count_of_done_tasks = len(bundle.task_set.all().filter(current_status=3))
    count_of_all_tasks = len(bundle.task_set.all())
    return (count_of_done_tasks / count_of_all_tasks * 100) if count_of_all_tasks != 0 else 0


def change_task_status_and_return_context(data):
    task_title = data.get('task_move_right') if data.get('task_move_right') else data.get('task_move_left')
    task = get_task_by_name(task_title)
    bundle_name = task.parent_bundle
    task.update_status(1 if data.get('task_move_right') else -1)
    context = {'tasks_from_bundle': get_bundle_by_name(bundle_name).task_set.all(),
               'progress': calculate_bundle_progress(bundle_name),
               'bundle_name': bundle_name}
    return context


def add_description_to_task_and_return_bundle(task_id, description):
    task = Task.objects.filter(id=task_id)[0]
    task.task_description = description
    task.save()
    return task.parent_bundle


def change_task_title_and_return_bundle(task_id, new_title):
    task = Task.objects.filter(id=task_id)[0]
    task.task_title = new_title
    task.save()
    return task.parent_bundle


def get_bundle_by_taskid(task_id):
    return Task.objects.filter(id=task_id)[0].parent_bundle


def delete_task_by_id(task_id):
    task = Task.objects.filter(id=task_id)[0]
    task.delete()
