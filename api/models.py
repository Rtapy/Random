from django.db import models
from django.conf import settings

class Project(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField(blank=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE, 
        related_name="projects",
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    

class Task(models.Model):
    class Status(models.TextChoices):
        TODO = "todo", "Todo"
        DOING = "doing", "Doing"
        DONE = "done", "Done"

    project = models.ForeignKey(
        Project, 
        on_delete=models.CASCADE,
        related_name="tasks",
    )
    title = models.CharField(max_length=250)
    status = models.CharField(max_length=10, choices=Status.choices, default=Status.TODO)
    priority = models.PositiveSmallIntegerField(default=3) 
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="tasks",
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    

class Comment(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name="comments")
    body = models.TextField()
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="comments",
    )
    created_at = models.DateTimeField(auto_now_add=True)

