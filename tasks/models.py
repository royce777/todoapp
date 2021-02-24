from django.db import models

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)
    #true -> the task will be displayed
    #false -> will be stored in DB, but not displayed
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title
    