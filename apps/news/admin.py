from django.contrib import admin
from parler.admin import TranslatableAdmin
from .models import News


@admin.register(News)
class NewsAdmin(TranslatableAdmin):
    list_display = (
        'id',
        'title',
        'date',
    )

    list_filter = (
        'date',
    )

    search_fields = (
        'translations__title',
        'translations__content',
    )

    date_hierarchy = 'date'

    ordering = ('-date',)

    fieldsets = (
        (None, {
            'fields': (
                'date',
                'image',
            )
        }),
        ('Переводы', {
            'fields': (
                'title',
                'content',
            )
        }),
    )

    readonly_fields = ()

    def title(self, obj):
        return obj.safe_translation_getter('title', any_language=True)

    title.short_description = "Заголовок"
