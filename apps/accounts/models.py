# apps/accounts/models.py
from django.db import models
import os
from datetime import datetime
from django.utils.text import slugify
from django.contrib.auth.models import User
from django_countries.fields import CountryField
import uuid

def user_file_path(instance, filename, folder):
    if instance.user_id:
        name_slug = slugify(f"{instance.user.first_name}_{instance.user.last_name}") or instance.user.username
    else:
        name_slug = "unknown_user"

    base, ext = os.path.splitext(filename)
    unique = uuid.uuid4().hex[:8]
    new_filename = f"{base}_{unique}{ext}"
    return os.path.join(name_slug, folder, new_filename)



def photo_path(instance, filename):
    return user_file_path(instance, filename, 'photo')

def passport_copy_path(instance, filename):
    return user_file_path(instance, filename, 'passport_copy')

def employment_verification_path(instance, filename):
    return user_file_path(instance, filename, 'employment_verification')



class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile", verbose_name="Пользователь", help_text="Связанный аккаунт пользователя")
    
	DEGREE_CHOICES = [
		('bachelor', "Bachelor's"),
		('master', "Master's"),
		('phd', "PhD"),
		('other', "Other"),
	]
    # Персональные данные
	first_name = models.CharField(max_length=100, verbose_name="Имя", help_text="Введите ваше имя")  
	last_name = models.CharField(max_length=100, verbose_name="Фамилия", help_text="Введите вашу фамилию")   
	father_name = models.CharField(max_length=50, blank=True, null=True, verbose_name="Отчество", help_text="Введите отчество (необязательно)")  
	company = models.CharField(max_length=255, blank=True, null=True, verbose_name="Компания", help_text="Название вашей компании")
	position = models.CharField(max_length=255, blank=True, null=True, verbose_name="Должность", help_text="Ваша должность в компании")  
	birth_date = models.DateField(blank=True, null=True, verbose_name="Дата рождения", help_text="Формат: ГГГГ-ММ-ДД")
	country = CountryField(blank=True, null=True, verbose_name="Страна", help_text="Выберите вашу страну")
	address = models.TextField(blank=True, null=True, verbose_name="Адрес", help_text="Полный адрес проживания")
	passport_number = models.CharField(max_length=50, blank=True, null=True, verbose_name="Номер паспорта", help_text="Номер вашего паспорта")
	passport_issue_date = models.DateField(blank=True, null=True, verbose_name="Дата выдачи паспорта", help_text="Формат: ГГГГ-ММ-ДД")
	passport_expiry_date = models.DateField(blank=True, null=True, verbose_name="Дата окончания паспорта", help_text="Формат: ГГГГ-ММ-ДД")
	education_degree = models.CharField(max_length=100, blank=True, null=True, choices=DEGREE_CHOICES, verbose_name="Степень образования", help_text="Например: Bachelor's, Master's")
	education_institute = models.CharField(max_length=255, blank=True, null=True, verbose_name="Учебное заведение", help_text="Название университета или колледжа")
	specialization = models.CharField(max_length=255, blank=True, null=True, verbose_name="Специализация", help_text="Ваша специализация или факультет")
	website = models.URLField(blank=True, null=True, verbose_name="Веб-сайт", help_text="Если есть личный сайт или компания")

	# Файлы
	photo = models.ImageField(upload_to=photo_path, blank=True, null=True, verbose_name="Фото", help_text="Загрузите ваше фото")
	passport_copy = models.FileField(upload_to=passport_copy_path, blank=True, null=True, verbose_name="Копия паспорта", help_text="Загрузите скан вашего паспорта")
	employment_verification = models.FileField(upload_to=employment_verification_path, blank=True, null=True, verbose_name="Справка с работы", help_text="Загрузите подтверждение занятости")

	def __str__(self):
		return f"{self.user.username} Profile"
