from django.contrib import admin
from parler.admin import TranslatableAdmin
from .models import Intro, About, Tabs, PartnershipType, Partner, PartnerLevel, FileResource, Sector
from django.utils.html import format_html

@admin.register(Intro)
class IntroAdmin(admin.ModelAdmin):
	list_display = ('video',)


@admin.register(About)
class AboutAdmin(TranslatableAdmin):
	list_display = ('title', 'image')


@admin.register(Tabs)
class TabsAdmin(admin.ModelAdmin):
	list_display = ('img',)


@admin.register(PartnershipType)
class PartnershipTypeAdmin(TranslatableAdmin):
	list_display = ('name',)


@admin.register(Partner)
class PartnerAdmin(TranslatableAdmin):
	list_display = ('name', 'partnership_type', 'logo', 'order')
	list_filter = ('partnership_type',)

@admin.register(PartnerLevel)
class PartnerLevelAdmin(TranslatableAdmin):
	list_display = ('name', 'priority')
	ordering = ('priority',)


@admin.register(FileResource)
class FileResourceAdmin(TranslatableAdmin):
    # Показываем эти поля в списке
    list_display = ('name', 'resource_type', 'is_active', 'created_at')
    list_filter = ('resource_type', 'is_active')
    search_fields = ('translations__name',)
    ordering = ('-created_at',)

    # Поля, которые будут редактироваться в админке
    fieldsets = (
        (None, {
            'fields': ('resource_type', 'is_active', 'file')
        }),
        ('Переводы', {
            'fields': ('name', 'description'),
            'classes': ('collapse',)  # Можно свернуть
        }),
    )

    def get_prepopulated_fields(self, request, obj=None):
        # Можно добавить автозаполнение slug или другого поля, если будет
        return {}
	

@admin.register(Sector)
class SectorAdmin(TranslatableAdmin):
    list_display = ('name', 'created_at', 'updated_at', 'preview_image')
    search_fields = ('translations__name',)
    readonly_fields = ('preview_image',)

    def preview_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width: 100px; height:auto; border-radius:5px;" />', obj.image.url)
        return "-"
    preview_image.short_description = "Фото сектора"