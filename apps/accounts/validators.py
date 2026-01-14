from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_file_size(file):
    max_size = 15 * 1024 * 1024  # 10 MB

    if file.size > max_size:
        raise ValidationError(
            _("File size must not exceed 15 MB.")
        )
