from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFit

class Gallery(models.Model):
	image = models.ImageField(upload_to='gallery/%Y/%m/%d/')
	image_compressed = ImageSpecField(
        source='image',
        processors=[ResizeToFit(1920, 1920)],
        format='JPEG',
        options={
            'quality': 75,
            'optimize': True,
        }
    )