from django.db import models

# Create your models here.

class Portfolio(models.Model):
    title=models.CharField(max_length=255)
    description=models.TextField(blank=True,max_length=500)
    image=models.ImageField(upload_to='portfolio/media',blank=True)
    url=models.URLField(blank=True)

    def __str__(self):
        return self.title

