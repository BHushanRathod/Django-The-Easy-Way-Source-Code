from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=255, default='')
    image = models.ImageField(default='', blank=True, upload_to='images')
