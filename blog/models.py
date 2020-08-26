from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, max_length=500)
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title