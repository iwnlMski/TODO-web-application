from django.db import models


# Create your models here.
class Bundle(models.Model):
    name = models.CharField(max_length=256, unique=True)
    created_date = models.DateTimeField('date of creation')

    def __str__(self):
        return self.name


class Task(models.Model):
    name_of_bundle = models.ForeignKey(Bundle, on_delete=models.CASCADE)
    task_description = models.CharField(max_length=256)

    STATUS_CHOICES = (
        (1, 'TODO'),
        (2, 'IN_PROGRESS'),
        (3, 'DONE')
    )
    current_status = models.IntegerField(choices=STATUS_CHOICES, default=1)

    def update_status(self, new_state_number):
        self.current_status = new_state_number

    def __str__(self):
        return self.task_description
