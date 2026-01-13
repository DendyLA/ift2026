from django.contrib import admin
from django.utils.html import format_html
from django.urls import path
from import_export.admin import ExportMixin

from .models import Profile, CatalogEntry
from .admin_resources import ProfileResource

@admin.register(Profile)
class ProfileAdmin(ExportMixin, admin.ModelAdmin):
	resource_class = ProfileResource
	# Что видно в списке
	list_display = (
		"user",
		"first_name",
		"last_name",
		"country",
		"company",
		"position",
		'need_visa'
	)

	# Фильтры справа
	list_filter = (
		"country",                # фильтр по стране
		"education_degree",       # фильтр по образованию
		"has_paid_delegate_fee",  # фильтр по оплате делегатского взноса
		"visa_processed",         # фильтр по обработке визы
		'need_visa'
	)

	# Поиск сверху
	search_fields = (
		"user__username",
		"first_name",   # поиск по имени
		"last_name",    # поиск по фамилии
		"company",
	)

	# Поля только для чтения
	readonly_fields = ("photo_preview",)
	ordering = ("country", "last_name", "first_name", 'need_visa')
	# Группировка полей (ВАЖНО для красоты)
	fieldsets = (
		("Пользователь", {
			"fields": ("user",)
		}),

		("Персональные данные", {
			"fields": (
				"first_name",
				"last_name",
				"father_name",
				"birth_date",
				"country",
				"address",
			)
		}),

		("Работа", {
			"fields": (
				"company",
				"position",
				"employment_verification",
			)
		}),

		("Образование", {
			"fields": (
				"education_degree",
				"education_institute",
				"specialization",
				"diploma_scan",
			)
		}),

		("Паспортные данные", {
			"fields": (
				"passport_number",
				"passport_issue_date",
				"passport_expiry_date",
				"passport_copy",
			)
		}),

		("Фото", {
			"fields": (
				"photo",
				"photo_preview",
			)
		}),

		("Дополнительно", {
			"fields": ("website",'need_visa')
		}),
		("Корпоративная информация", {
			"fields": ("has_paid_delegate_fee", "visa_processed")
		}),
	)

	def photo_preview(self, obj):
		if obj.photo:
			return format_html(
				'<img src="{}" style="max-height: 150px; border-radius: 8px;" />',
				obj.photo.url
			)
		return "Нет фото"



	photo_preview.short_description = "Превью фото"





@admin.register(CatalogEntry)
class CatalogEntryAdmin(admin.ModelAdmin):
	list_display = ('id', 'description', "photo_preview", 'created_at', 'updated_at')
	list_display_links = ('id', 'description', "photo_preview",)
	readonly_fields = ('created_at', 'updated_at')

	def photo_preview(self, obj):
		if obj.img:
			return format_html(
				'<img src="{}" style="max-height: 150px; border-radius: 8px;" />',
				obj.img.url
			)
		return "Нет фото"