from django.db import models
from django.utils import timezone
from parler.models import TranslatableModel, TranslatedFields
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.text import slugify
from django.urls import reverse
import uuid
import os

from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from imagekit.processors import SmartResize
from imagekit.processors import Adjust

class News(TranslatableModel):
	translations = TranslatedFields(
		title = models.CharField(max_length=255, verbose_name="Title"),
		content = RichTextUploadingField(verbose_name="Content")
	)

	date = models.DateField(default=timezone.now, verbose_name="Date")
	image = models.ImageField(upload_to='news/%Y/%m/%d', blank=True, null=True, verbose_name="Image")
	# Оптимизированная версия
	image_preview = ImageSpecField(
		source='image',
		processors=[
			SmartResize(1200, 630),  # 🔥 идеально для новостей + OG
			Adjust(sharpness=1.2),
		],
		format='JPEG',
		options={'quality': 85},
	)
	slug = models.SlugField(max_length=255, unique=True, blank=True)


	class Meta:
		ordering = ['-date']
		verbose_name = "News"
		verbose_name_plural = "News"
        

	def save(self, *args, **kwargs):
		# Создаем slug из заголовка на основном языке
		if not self.slug:
			self.slug = slugify(self.safe_translation_getter('title', any_language=True))
		super().save(*args, **kwargs)

	def __str__(self):
		return self.safe_translation_getter('title', any_language=True) or ''
