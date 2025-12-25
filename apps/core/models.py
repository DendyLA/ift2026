from django.db import models
from parler.models import TranslatableModel, TranslatedFields
from ckeditor.fields import RichTextField

class Intro(models.Model):
	video = models.FileField(upload_to='intro_videos/%Y/%m/%d', verbose_name='Intro Video')


class About(TranslatableModel):
	translations = TranslatedFields(
		title=models.CharField(max_length=200, verbose_name='Title', blank=True, null=True),
		description=RichTextField(verbose_name='Description', blank=True, null=True),
	)
	image = models.ImageField(upload_to='about_images/%Y/%m/%d', verbose_name='About Image')



