from django.contrib import admin
from parler.admin import TranslatableAdmin
from .models import Intro, About, Tabs, PartnershipType, Partner, PartnerLevel

@admin.register(Intro)
class IntroAdmin(admin.ModelAdmin):
	list_display = ('video',)


@admin.register(About)
class AboutAdmin(TranslatableAdmin):
	list_display = ('title', 'image')


@admin.register(Tabs)
class TabsAdmin(admin.ModelAdmin):
	list_display = ('img',)


@admin.register(PartnershipType)
class PartnershipTypeAdmin(TranslatableAdmin):
	list_display = ('name',)


@admin.register(Partner)
class PartnerAdmin(TranslatableAdmin):
	list_display = ('name', 'partnership_type', 'logo')
	list_filter = ('partnership_type',)

@admin.register(PartnerLevel)
class PartnerLevelAdmin(TranslatableAdmin):
	list_display = ('name', 'priority')
	ordering = ('priority',)