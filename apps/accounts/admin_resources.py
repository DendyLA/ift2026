from import_export import resources, fields
from django.conf import settings
from .models import Profile


class ProfileResource(resources.ModelResource):

    email = fields.Field(column_name="E-mail")
    phone = fields.Field(attribute="phone", column_name="Телефон")

    first_name = fields.Field(attribute="first_name", column_name="Имя")
    last_name = fields.Field(attribute="last_name", column_name="Фамилия")
    father_name = fields.Field(attribute="father_name", column_name="Отчество")
    birth_date = fields.Field(attribute="birth_date", column_name="Дата рождения")
    country = fields.Field(attribute="country", column_name="Страна")
    address = fields.Field(attribute="address", column_name="Адрес")
    company = fields.Field(attribute="company", column_name="Компания")
    position = fields.Field(attribute="position", column_name="Должность")
    website = fields.Field(attribute="website", column_name="Веб-сайт")
    education_degree = fields.Field(attribute="education_degree", column_name="Степень образования")
    education_institute = fields.Field(attribute="education_institute", column_name="Учебное заведение")
    specialization = fields.Field(attribute="specialization", column_name="Специализация")

    need_visa = fields.Field(attribute="need_visa", column_name="Нужна виза")
    has_paid_delegate_fee = fields.Field(attribute="has_paid_delegate_fee", column_name="Оплатил делегатский взнос")
    visa_processed = fields.Field(attribute="visa_processed", column_name="Виза обработана")

    photo_url = fields.Field(column_name="Фото")
    passport_copy_url = fields.Field(column_name="Копия паспорта")
    employment_verification_url = fields.Field(column_name="Справка с работы")
    diploma_scan_url = fields.Field(column_name="Диплом")

    # ===== DEHYDRATE =====

    def dehydrate_email(self, obj):
        return obj.user.email if obj.user else ""

    def dehydrate_phone(self, obj):
        return obj.phone or ""

    def dehydrate_first_name(self, obj):
        return obj.first_name or ""

    def dehydrate_last_name(self, obj):
        return obj.last_name or ""

    def dehydrate_father_name(self, obj):
        return obj.father_name or ""

    def dehydrate_birth_date(self, obj):
        return obj.birth_date.strftime("%d.%m.%Y") if obj.birth_date else ""

    def dehydrate_country(self, obj):
        return obj.country.name if obj.country else ""

    def dehydrate_address(self, obj):
        return obj.address or ""

    def dehydrate_company(self, obj):
        return obj.company or ""

    def dehydrate_position(self, obj):
        return obj.position or ""

    def dehydrate_website(self, obj):
        return obj.website or ""

    def dehydrate_education_degree(self, obj):
        return obj.get_education_degree_display() if obj.education_degree else ""

    def dehydrate_education_institute(self, obj):
        return obj.education_institute or ""

    def dehydrate_specialization(self, obj):
        return obj.specialization or ""

    def yes_no(self, value):
        return "Да" if value else "Нет"

    def dehydrate_need_visa(self, obj):
        return self.yes_no(obj.need_visa)

    def dehydrate_has_paid_delegate_fee(self, obj):
        return self.yes_no(obj.has_paid_delegate_fee)

    def dehydrate_visa_processed(self, obj):
        return self.yes_no(obj.visa_processed)

    def full_url(self, path):
        if not path:
            return ""
        return f"{settings.SITE_DOMAIN}{path}"

    def dehydrate_photo_url(self, obj):
        return self.full_url(obj.photo.url if obj.photo else "")

    def dehydrate_passport_copy_url(self, obj):
        return self.full_url(obj.passport_copy.url if obj.passport_copy else "")

    def dehydrate_employment_verification_url(self, obj):
        return self.full_url(obj.employment_verification.url if obj.employment_verification else "")

    def dehydrate_diploma_scan_url(self, obj):
        return self.full_url(obj.diploma_scan.url if obj.diploma_scan else "")

    class Meta:
        model = Profile
        fields = (
            "first_name",
            "last_name",
            "father_name",
            "email",
            "phone",
            "birth_date",
            "country",
            "address",
            "company",
            "position",
            "website",
            "education_degree",
            "education_institute",
            "specialization",
            "need_visa",
            "has_paid_delegate_fee",
            "visa_processed",
            "photo_url",
            "passport_copy_url",
            "employment_verification_url",
            "diploma_scan_url",
        )

        export_order = fields

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.exclude(user__is_staff=True).exclude(user__is_superuser=True)
