from allauth.account.forms import LoginForm, SignupForm, ResetPasswordForm, ResetPasswordKeyForm
from django import forms
from django.utils.translation import gettext_lazy as _
from django_countries.widgets import CountrySelectWidget

from .models import Profile, CatalogEntry
from django.core.validators import RegexValidator

english_validator = RegexValidator(
    regex=r'^[A-Za-z0-9\s.,\-_/()]*$',
    message="Only English letters are allowed."
)


class CustomLoginForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # поле login (email)
        self.fields["login"].label = _("Email")
        self.fields["login"].widget.attrs.update({
            "class": "auth__input",
            "placeholder": " ",
            "autocomplete": "email",
        })

        # поле password
        self.fields["password"].label = _("Password")
        self.fields["password"].widget.attrs.update({
            "class": "auth__input",
            "placeholder": " ",
            "autocomplete": "current-password",
        })
        
		# поле remember (чекбокс)
        if "remember" in self.fields:
            self.fields["remember"].widget.attrs.update({
                "class": "auth__check",  # отдельный класс для чекбокса
            })



class CustomSignupForm(SignupForm):
    agree_terms = forms.BooleanField(
        required=True,
        label=_("I have read and agree to the Privacy Policy and Terms of Service"),
        widget=forms.CheckboxInput(attrs={
            "class": "auth__check",
        })
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["email"].label = _("Email")
        self.fields["email"].widget.attrs.update({
            "class": "auth__input",
            "placeholder": " ",
            "autocomplete": "email",
        })

        self.fields["password1"].label = _("Password")
        self.fields["password1"].widget.attrs.update({
            "class": "auth__input",
            "placeholder": " ",
            "autocomplete": "new-password",
        })

        self.fields["password2"].label = _("Confirm Password")
        self.fields["password2"].widget.attrs.update({
            "class": "auth__input",
            "placeholder": " ",
            "autocomplete": "new-password",
        })
        

class CustomPasswordResetForm(ResetPasswordForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({
            "class": "auth__input",
            "placeholder": " ",
            "autocomplete": "email",
        })
        self.fields['email'].label = _("Email")
        

class CustomPasswordResetFromKeyForm(ResetPasswordKeyForm):
    """
    Форма для установки нового пароля по ссылке из письма.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Новые пароли
        self.fields['password1'].label = _("New Password")
        self.fields['password1'].widget.attrs.update({
            "class": "auth__input",
            "placeholder": " ",
            "autocomplete": "new-password",
        })

        self.fields['password2'].label = _("Confirm Password")
        self.fields['password2'].widget.attrs.update({
            "class": "auth__input",
            "placeholder": " ",
            "autocomplete": "new-password",
        })
        

# profile


# apps/accounts/forms.py

class ProfileForm(forms.ModelForm):
	need_visa = forms.BooleanField(
		required=False,
		label=_("Visa "),
		widget=forms.CheckboxInput(attrs={
			"class": "profile__input",
			"id": "id_need_visa"
		})
	)

	class Meta:
		model = Profile
		exclude = ['user', 'has_paid_delegate_fee', 'visa_processed']
		widgets = {
			'first_name': forms.TextInput(attrs={'class': 'profile__input'}),
			'last_name': forms.TextInput(attrs={'class': 'profile__input'}),
			'father_name': forms.TextInput(attrs={'class': 'profile__input'}),
			'birth_date': forms.DateInput(attrs={'type': 'date', 'class': 'profile__input'}, format='%Y-%m-%d'),
			'phone': forms.TextInput(attrs={'class': 'profile__input'}),
			'company': forms.TextInput(attrs={'class': 'profile__input'}),
			'position': forms.TextInput(attrs={'class': 'profile__input'}),
			'country': CountrySelectWidget(attrs={'class': 'profile__input'}),
			'address': forms.TextInput(attrs={'class': 'profile__input'}),
			'passport_number': forms.TextInput(attrs={'class': 'profile__input'}),
			'passport_issue_date': forms.DateInput(attrs={'type': 'date', 'class': 'profile__input'}),
			'passport_expiry_date': forms.DateInput(attrs={'type': 'date', 'class': 'profile__input'}),
			'education_degree': forms.Select(attrs={'class': 'profile__input'}),
			'education_institute': forms.TextInput(attrs={'class': 'profile__input'}),
			'specialization': forms.TextInput(attrs={'class': 'profile__input'}),
			'website': forms.URLInput(attrs={'class': 'profile__input'}),
			'photo': forms.FileInput(attrs={'class': 'profile__input'}),
			'passport_copy': forms.FileInput(attrs={'class': 'profile__input'}),
			'employment_verification': forms.FileInput(attrs={'class': 'profile__input'}),
			'diploma_scan': forms.FileInput(attrs={'class': 'profile__input'}),
		}
		help_texts = {
			'passport_copy': 'Max file size: 5 MB',
			'diploma_scan': 'Max file size: 5 MB',
		}

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

		# 🔹 Переводимые лейблы
		self.fields['first_name'].label = _("First name")
		self.fields['last_name'].label = _("Last name")
		self.fields['father_name'].label = _("Father name")
		self.fields['birth_date'].label = _("Date of birth")
		self.fields['company'].label = _("Company")
		self.fields['position'].label = _("Position")
		self.fields['country'].label = _("Country")
		self.fields['address'].label = _("Address")
		self.fields['passport_number'].label = _("Passport number")
		self.fields['passport_issue_date'].label = _("Passport issue date")
		self.fields['passport_expiry_date'].label = _("Passport expiry date")
		self.fields['education_degree'].label = _("Education level")
		self.fields['education_institute'].label = _("Educational institution")
		self.fields['specialization'].label = _("Specialization")
		self.fields['website'].label = _("Website")
		self.fields['photo'].label = _("Profile photo")
		self.fields['passport_copy'].label = _("Passport photo")
		self.fields['employment_verification'].label = _("Employment verification photo")
		self.fields['diploma_scan'].label = _("Diploma photo")

		# 🔹 Формат дат при редактировании
		for date_field in ['birth_date', 'passport_issue_date', 'passport_expiry_date']:
			if self.instance and getattr(self.instance, date_field):
				self.initial[date_field] = getattr(self.instance, date_field).strftime('%Y-%m-%d')

		# 🔹 Переводимые choices
		country_choices = list(self.fields['country'].choices)
		if country_choices and country_choices[0][0] == '':
			country_choices.pop(0)
		self.fields['country'].choices = [('', _("Select country"))] + country_choices

		edu_choices = list(self.fields['education_degree'].choices)
		if edu_choices and edu_choices[0][0] == '':
			edu_choices.pop(0)
		self.fields['education_degree'].choices = [('', _("Select level"))] + edu_choices
            

		english_fields = [
			"first_name",
			"last_name",
			"father_name",
			"company",
			"position",
			"address",
			"passport_number",
			"education_institute",
			"specialization",
		]

		for field in english_fields:
			if field in self.fields:
				self.fields[field].validators.append(english_validator)
        



class CatalogEntryForm(forms.ModelForm):
    class Meta:
        model = CatalogEntry
        exclude = ["profile"]
        widgets = {
            "description": forms.Textarea(attrs={"class": "profile__input", "rows": 5}),
            "img": forms.FileInput(attrs={"class": "profile__input", "accept": "image/*"}),
        }

