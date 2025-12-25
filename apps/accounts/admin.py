from django.contrib import admin
from .models import Profile
from django.utils.html import format_html

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    # Что видно в списке
    list_display = (
        "user",
        "first_name",
        "last_name",
        "country",
        "company",
        "position",
    )

    # Фильтры справа
    list_filter = (
        "country",
        "education_degree",
    )

    # Поиск сверху
    search_fields = (
        "user__username",
        "first_name",
        "last_name",
        "company",
    )

    # Поля только для чтения
    readonly_fields = ("photo_preview",)

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
            "fields": ("website",)
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
