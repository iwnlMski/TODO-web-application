from django.db import models


# Create your models here.
class Bundle(models.Model):
    name = models.CharField(max_length=256, unique=True)
    created_date = models.DateTimeField('date of creation')
    # tasks_done = models.IntegerField(default=0)
    # tasks_in_progress = models.IntegerField(default=0)
    # tasks_to_do = models.IntegerField(default=0)


class Task(models.Model):
    name_of_bundle = models.ForeignKey(Bundle, on_delete=models.CASCADE)
    task_to_be_done = models.CharField(max_length=256)