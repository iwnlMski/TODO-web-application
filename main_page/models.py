from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Bundle(models.Model):
    name = models.CharField(max_length=256, unique=True)
    created_date = models.DateTimeField('date of creation')
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Task(models.Model):
    parent_bundle = models.ForeignKey(Bundle, on_delete=models.CASCADE)
    task_title = models.CharField(max_length=64)
    task_description = models.CharField(max_length=512, default='')

    STATUS_CHOICES = (
        (1, 'TODO'),
        (2, 'IN_PROGRESS'),
        (3, 'DONE')
    )
    current_status = models.IntegerField(choices=STATUS_CHOICES, default=1)

    def update_status(self, new_state_number):
        if 0 < (self.current_status + new_state_number) < 4:
            self.current_status += new_state_number
            self.save()

    def __str__(self):
        return self.task_title
