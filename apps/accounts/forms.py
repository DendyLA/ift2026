from allauth.account.forms import LoginForm, SignupForm, ResetPasswordForm, ResetPasswordKeyForm
from django import forms
from django.utils.translation import gettext_lazy as _
from django_countries.widgets import CountrySelectWidget

from .models import Profile


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

	class Meta:
		model = Profile
		exclude = ['user']  # user назначается автоматически
		widgets = {
			'first_name': forms.TextInput(attrs={'class': 'profile__input', 'placeholder': ''}),
			'last_name': forms.TextInput(attrs={'class': 'profile__input', 'placeholder': ''}),
			'father_name': forms.TextInput(attrs={'class': 'profile__input', 'placeholder': ''}),
			'birth_date': forms.DateInput(attrs={'type': 'date', 'class': 'profile__input'}, format='%Y-%m-%d'),
			'company': forms.TextInput(attrs={'class': 'profile__input', 'placeholder': ''}),
			'position': forms.TextInput(attrs={'class': 'profile__input', 'placeholder': ''}),
			'country': CountrySelectWidget(attrs={'class': 'profile__input'}),
			'address': forms.TextInput(attrs={'class': 'profile__input', 'placeholder': ''}),
			'passport_number': forms.TextInput(attrs={'class': 'profile__input', 'placeholder': ''}),
			'passport_issue_date': forms.DateInput(attrs={'type': 'date', 'class': 'profile__input'}),
			'passport_expiry_date': forms.DateInput(attrs={'type': 'date', 'class': 'profile__input'}),
			'education_degree': forms.Select(attrs={'class': 'profile__input'}),
			'education_institute': forms.TextInput(attrs={'class': 'profile__input', 'placeholder': ''}),
			'specialization': forms.TextInput(attrs={'class': 'profile__input', 'placeholder': ''}),
			'website': forms.URLInput(attrs={'class': 'profile__input', 'placeholder': ''}),
			'photo': forms.FileInput(attrs={'class': 'profile__input', }),
			'passport_copy': forms.FileInput(attrs={'class': 'profile__input', }),
            'employment_verification': forms.FileInput(attrs={'class': 'profile__input', }),
		}
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		# Подставляем формат даты при редактировании
		for date_field in ['birth_date', 'passport_issue_date', 'passport_expiry_date']:
			if self.instance and getattr(self.instance, date_field):
				self.initial[date_field] = getattr(self.instance, date_field).strftime('%Y-%m-%d')

		# Убираем стандартное '--------' у страны и ставим плейсхолдер
		country_choices = list(self.fields['country'].choices)
		if country_choices and country_choices[0][0] == '':
			country_choices.pop(0)  # удаляем пустую опцию
		self.fields['country'].choices = [('', 'Выберите страну')] + country_choices

		# Для уровня образования
		edu_choices = list(self.fields['education_degree'].choices)
		if edu_choices and edu_choices[0][0] == '':
			edu_choices.pop(0)
		self.fields['education_degree'].choices = [('', 'Выберите уровень')] + edu_choices