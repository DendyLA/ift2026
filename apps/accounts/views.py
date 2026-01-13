# apps/accounts/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
import pdfkit
import os
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.shortcuts import get_object_or_404

from .forms import ProfileForm, CatalogEntryForm
from .models import Profile, CatalogEntry

@login_required
def profile_view(request):
    profile, created = Profile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user  # обязательно привязать user
            profile.save()  # теперь instance.user есть, upload_to сработает правильно
            form.save_m2m()
            return redirect('accounts:profile')
    else:
        form = ProfileForm(instance=profile)

    return render(request, 'accounts/profile.html', {'form': form})





@login_required
def catalog_edit_view(request):
    profile = request.user.profile

    catalog, _ = CatalogEntry.objects.get_or_create(profile=profile)

    if request.method == "POST":
        form = CatalogEntryForm(request.POST, request.FILES, instance=catalog)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.profile = profile  # обязательно привязываем профиль
            obj.save()
            return redirect("accounts:catalog_edit")
    else:
        form = CatalogEntryForm(instance=catalog)

    return render(request, "accounts/catalog.html", {"form": form})
