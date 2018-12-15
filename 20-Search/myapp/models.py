from django.db import models

class Tag(models.Model):

    title = models.CharField(max_length=255, default='')

    def __str__(self):
        return self.title

class Flower(models.Model):
    title = models.CharField(max_length=255, default='')
    description = models.TextField(default='')
    tags = models.ManyToManyField(Tag)
    
    def __str__(self):
        return self.title
