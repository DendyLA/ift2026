from django.db import models
from parler.models import TranslatableModel, TranslatedFields
from ckeditor.fields import RichTextField
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from django.urls import reverse

class Intro(models.Model):
	video = models.FileField(upload_to='intro_videos/%Y/%m/%d', verbose_name='Intro Video')


class About(TranslatableModel):
	translations = TranslatedFields(
		title=models.CharField(max_length=200, verbose_name='Title', blank=True, null=True),
		description=RichTextField(verbose_name='Description', blank=True, null=True),
	)
	image = models.ImageField(upload_to='about_images/%Y/%m/%d', verbose_name='About Image')

	def get_absolute_url(self):
		return reverse('core:index')


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



class Partner(TranslatableModel):
	translations = TranslatedFields(
		name=models.CharField(max_length=255, verbose_name='Partner Name', blank=True, null=True),	
	)
	logo = models.ImageField(upload_to='partners/logo/%Y/%m/%d')
	partnership_type = models.ForeignKey(
		PartnershipType,
		on_delete=models.CASCADE,
		related_name='partners'
	)

	order = models.PositiveIntegerField(
        default=0,
        verbose_name="Порядок",
        help_text="Чем меньше число — тем выше отображается"
    )

	level = models.ForeignKey(
		PartnerLevel,
		on_delete=models.SET_NULL,
		null=True,
		blank=True,
		related_name='partners'
	)
	link = models.URLField(verbose_name='ссылка', blank=True, null=True)

	def get_absolute_url(self):
		return reverse('core:index')


	def __str__(self):
		return self.safe_translation_getter('name', any_language=True) or ''




class FileResource(TranslatableModel):
    """
    Модель для PDF-файлов вроде брошюр и тревел-гайдов.
    Каждый файл можно загрузить отдельно для разных языков.
    """
    translations = TranslatedFields(
        name=models.CharField(max_length=255, blank=True, null=True),
        description=models.TextField(blank=True, null=True),
        file=models.FileField(
            upload_to='files/',
            blank=True,
            null=True,
            help_text="Upload a PDF file for this language"
        )
    )

    RESOURCE_TYPE_CHOICES = [
        ('brochure', 'Brochure'),
        ('travel_guide', 'Travel Guide'),
		('off_support', 'Official Support'),
		('meet_req', 'Meeting Request'),
		('investment', 'Investors Guide '),
    ]
    resource_type = models.CharField(
        max_length=50,
        choices=RESOURCE_TYPE_CHOICES,
        default='brochure'
    )

    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "File Resource"
        verbose_name_plural = "File Resources"
        ordering = ['-created_at']

    def __str__(self):
        return self.safe_translation_getter('name', any_language=True) or str(self.id)





def sector_image_path(instance, filename):
    # загружаем изображения в папку sectors
    import os, uuid
    base, ext = os.path.splitext(filename)
    unique = uuid.uuid4().hex[:8]
    return f"sectors/{base}_{unique}{ext}"

class Sector(TranslatableModel):
    translations = TranslatedFields(
        name=models.CharField(max_length=150, verbose_name="Название сектора"),
        description=models.TextField(verbose_name="Описание сектора", blank=True, null=True)
    )
    image = models.ImageField(upload_to=sector_image_path, verbose_name="Фото сектора", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

    class Meta:
        verbose_name = "Сектор"
        verbose_name_plural = "Секторы"
        ordering = ['id']

    def __str__(self):
        return self.safe_translation_getter('name', any_language=True) or "Сектор"