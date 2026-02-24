from django.db import models
from parler.models import TranslatableModel, TranslatedFields
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from ckeditor_uploader.fields import RichTextUploadingField

class Person(TranslatableModel):
    """
    Переводимая модель для спикеров / персон
    """

    translations = TranslatedFields(
        name=models.CharField(
            max_length=255,
            blank=True,
            null=True
        ),
        position=models.CharField(
            max_length=255,
            blank=True,
            null=True
        ),
        session=models.CharField(
            max_length=255,
            blank=True,
            null=True
        ),
        biography=RichTextUploadingField(
            blank=True,
            null=True
        ),
    )

    # ===== IMAGES =====
    photo = models.ImageField(
        upload_to='persons/photo/%Y/%m/%d',
        blank=True,
        null=True
    )

    # уменьшенное фото (например для карточек)
    photo_small = ImageSpecField(
        source='photo',
        processors=[ResizeToFill(300, 300)],
        format='JPEG',
        options={'quality': 85}
    )

    logo = models.ImageField(
        upload_to='persons/logo/%Y/%m/%d',
        blank=True,
        null=True
    )

    # ===== SERVICE =====
    order = models.PositiveIntegerField(
        default=0
    )
    is_active = models.BooleanField(
        default=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        ordering = ['order', 'id']

    def __str__(self):
        return self.safe_translation_getter('name', any_language=True) or 'Person'
