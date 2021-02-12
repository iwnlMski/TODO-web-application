from django.db import models


# Create your models here.
class Bundle(models.Model):
    name = models.CharField(max_length=256, unique=True)
    created_date = models.DateTimeField('date of creation')

    # tasks_done = models.IntegerField(default=0)
    # tasks_in_progress = models.IntegerField(default=0)
    # tasks_to_do = models.IntegerField(default=0)
    def __str__(self):
        return self.name


class Task(models.Model):
    name_of_bundle = models.ForeignKey(Bundle, on_delete=models.CASCADE)
    task_description = models.CharField(max_length=256)

    def __str__(self):
        return self.task_description
