from django.db import models
from imagekit.models import ImageSpecField
from pilkit.processors import ResizeToFill

class Flower(models.Model):
    title = models.CharField(max_length=255, default='')
    description = models.TextField(default='')
    image = models.ImageField(default='', blank=True, upload_to='images')
    image_thumbnail = ImageSpecField(source='image',
		processors=[ResizeToFill(350, 200)],
		format='JPEG',
		options={'quality': 60})
    
    def __str__(self):
        return self.title
