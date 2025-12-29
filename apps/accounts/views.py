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




def profile_pdf_view(request, profile_id):
    profile = get_object_or_404(Profile, id=profile_id)

    # нормализуем пути файлов
    def file_path_url(file_field):
        if file_field:
            # абсолютный путь и заменяем \ на /
            return os.path.abspath(file_field.path).replace("\\", "/")
        return None

    context = {
        "profile": profile,
        "photo_path": file_path_url(profile.photo),
        "passport_copy_path": file_path_url(profile.passport_copy),
        "employment_verification_path": file_path_url(profile.employment_verification),
        "diploma_scan_path": file_path_url(profile.diploma_scan),
    }

    html = render_to_string("accounts/admin/profile_pdf.html", context)

    config = pdfkit.configuration(
        wkhtmltopdf=r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe"
    )

    pdf = pdfkit.from_string(html, False, configuration=config, options={
        "enable-local-file-access": True
    })

    response = HttpResponse(pdf, content_type="application/pdf")
    response['Content-Disposition'] = f'attachment; filename="profile_{profile.user.username}.pdf"'
    return response



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
