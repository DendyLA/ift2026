from django.contrib import admin
from parler.admin import TranslatableAdmin
from django.utils.html import format_html

from .models import Person


@admin.register(Person)
class PersonAdmin(TranslatableAdmin):
    # ===== СПИСОК =====
    list_display = (
        'preview_photo',
        'name_display',
        'position_display',
        'is_active',
        'order',
    )

    list_display_links = ('preview_photo', 'name_display')
    list_editable = ('is_active', 'order')
    list_filter = ('is_active',)
    search_fields = (
        'translations__name',
        'translations__position',
        'translations__biography',
    )

    ordering = ('order', 'id')

    # ===== ФОРМА =====
    fieldsets = (
        ('Основная информация', {
            'fields': (
                'name',
                'position',
                'session',
                'biography',
            )
        }),
        ('Медиа', {
            'fields': (
                'photo',
                'logo',
                'photo_preview',
            )
        }),
        ('Настройки', {
            'fields': (
                'order',
                'is_active',
            )
        }),
    )

    readonly_fields = ('photo_preview',)

    # ===== ПРЕВЬЮ ФОТО =====
    def preview_photo(self, obj):
        if obj.photo:
            return format_html(
                '<img src="{}" style="width:50px;height:50px;border-radius:50%;object-fit:cover;" />',
                obj.photo.url
            )
        return '—'

    preview_photo.short_description = 'Фото'

    def photo_preview(self, obj):
        if obj.photo:
            return format_html(
                '<img src="{}" style="max-width:300px;border-radius:12px;" />',
                obj.photo.url
            )
        return 'Фото не загружено'

    photo_preview.short_description = 'Предпросмотр'

    # ===== ПЕРЕВОДИМЫЕ ПОЛЯ В LIST =====
    def name_display(self, obj):
        return obj.safe_translation_getter('name', any_language=True)

    name_display.short_description = 'Имя'

    def position_display(self, obj):
        return obj.safe_translation_getter('position', any_language=True)

    position_display.short_description = 'Должность'
