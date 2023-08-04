
from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(default='')
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f"타이틀:{self.title}"
    




