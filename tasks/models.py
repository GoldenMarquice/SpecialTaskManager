from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

# class Status(models.Model):
#     name = models.CharField(max_length=128)
#     description = models.CharField(max_length=128)
    
#     def __str__(self):
#         return self.name

class Task(models.Model):
    summary = models.CharField(max_length=128)
    description = models.TextField()
    reporter = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    assignee = models.ForeignKey(
            get_user_model(),
            on_delete=models.CASCADE,
            related_name="assignee"
    )
    class Status(models.IntegerChoices):
        TODO = 0,("To Do")
        INPROGRESS = 1, ("In Progress")
        COMPLETED = 2, ("Completed")

    status = models.IntegerField(default=Status.TODO, choices=Status.choices)
    def __str__(self):
        return self.summary