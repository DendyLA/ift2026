from import_export import resources, fields
from django.conf import settings
from .models import Profile


class ProfileResource(resources.ModelResource):
    username = fields.Field(column_name="Username")

    photo_url = fields.Field(column_name="Photo")
    passport_copy_url = fields.Field(column_name="Passport Copy")
    employment_verification_url = fields.Field(column_name="Employment Verification")
    diploma_scan_url = fields.Field(column_name="Diploma Scan")

    def dehydrate_username(self, obj):
        return obj.user.username if obj.user else ""

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

        exclude = (
            "photo",
            "passport_copy",
            "employment_verification",
            "diploma_scan",
        )

        export_order = (
            "id",
            "username",
            "first_name",
            "last_name",
            "country",
            "company",
            "position",
            "has_paid_delegate_fee",
            "visa_processed",
            "photo_url",
            "passport_copy_url",
            "employment_verification_url",
            "diploma_scan_url",
        )
