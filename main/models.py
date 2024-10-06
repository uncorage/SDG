from django.db import models
from django.utils import timezone


class Goal(models.Model):
    number = models.PositiveIntegerField(unique=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='goal_images/')

    def __str__(self):
        return f'{self.number}. {self.title}'


class TaskActive(models.Model):
    goal = models.ForeignKey(Goal, on_delete=models.CASCADE, related_name='tasks')  # Changed related_name to 'tasks'
    title = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(default="Ashgabat", null=False, max_length=255)
    benefits_description = models.TextField(null=True, blank=True)
    date_created = models.DateField(default=timezone.now)

    def __str__(self):
        return f'Task for Goal: {self.goal.title}'  # Corrected the string representation


class ReportActive(models.Model):
    goal = models.ForeignKey(Goal, on_delete=models.CASCADE, related_name='reports')  # Kept related_name as 'reports'
    description = models.TextField()
    image_reportage = models.ImageField(upload_to='goal_report/')
    video_reportage = models.FileField(upload_to='goal_video/', blank=True, null=True)
    date_reported = models.DateField(default=timezone.now)

    def __str__(self):
        return f'Report for Goal: {self.goal.title}'