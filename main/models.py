from django.db import models

class Goal(models.Model):
    number = models.PositiveIntegerField(unique=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='goal_images/')

    def __str__(self):
        return f'{self.number}. {self.title}'