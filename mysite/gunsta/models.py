from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ProjectModel(models.Model):
    project_title = models.CharField(
        max_length=240
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    project_description = models.CharField(
        max_length=240,
        null=True
    )
    def __str__(self):
        return "(" + str(self.author.username) + ") " + self.project_title

class StepModel(models.Model):
    step_name = models.CharField(
        max_length=240
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    project = models.ForeignKey(
        ProjectModel,
        on_delete=models.CASCADE
    )
    status = models.CharField(
        max_length=240
    )
    def __str__(self):
        return "(" + str(self.author.username) + ") [" + str(self.project.project_title) + "] " + self.step_name