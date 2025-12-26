from django.db import models
from parler.models import TranslatableModel, TranslatedFields
from ckeditor.fields import RichTextField
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

class Intro(models.Model):
	video = models.FileField(upload_to='intro_videos/%Y/%m/%d', verbose_name='Intro Video')


class About(TranslatableModel):
	translations = TranslatedFields(
		title=models.CharField(max_length=200, verbose_name='Title', blank=True, null=True),
		description=RichTextField(verbose_name='Description', blank=True, null=True),
	)
	image = models.ImageField(upload_to='about_images/%Y/%m/%d', verbose_name='About Image')


class Tabs(models.Model):
	img = models.ImageField(upload_to='tabs_images/%Y/%m/%d', verbose_name='Tab Image')
	# Оптимизированная версия
	img_optimized = ImageSpecField(
		source='img',
		processors=[
			ResizeToFill(800, 800),  
		],
		format='WEBP',
    	options={'quality': 75}
	)

	def __str__(self):
		return f"Tab {self.id}" or " "


class PartnershipType(TranslatableModel):
    translations = TranslatedFields(
		name=models.CharField(max_length=100, verbose_name='Partnership Type Name')
	)

    def __str__(self):
        return self.name or " "
    

class PartnerLevel(TranslatableModel):
	translations = TranslatedFields(
		name=models.CharField(max_length=50, verbose_name='Partner Level Name')
	)
	slug = models.SlugField(
		max_length=50,
		unique=True,
		help_text='Используется для CSS классов (gold, silver, bronze)'
	)
	priority = models.PositiveIntegerField(default=0)

	def __str__(self):
		return self.name or ' '



class Partner(models.Model):
    name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='partners/logo/%Y/%m/%d')
    partnership_type = models.ForeignKey(
        PartnershipType,
        on_delete=models.CASCADE,
        related_name='partners'
    )

    level = models.ForeignKey(
        PartnerLevel,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='partners'
    )

    def __str__(self):
        return self.name or ' '



