# apps/accounts/urls.py
from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('', views.profile_view, name='profile'),
	path("company/", views.catalog_edit_view,name="catalog_edit"),
]
