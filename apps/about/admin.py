from django.contrib import admin
from .models import Gallery

@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
	list_display = ('id', 'image',)
	readonly_fields = ('image_compressed',)