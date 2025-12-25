from django.contrib import admin
from parler.admin import TranslatableAdmin
from .models import Intro, About

@admin.register(Intro)
class IntroAdmin(admin.ModelAdmin):
	list_display = ('video',)


@admin.register(About)
class AboutAdmin(TranslatableAdmin):
	list_display = ('title', 'image')

