from django.shortcuts import render


def index(request):
    return render(request, 'core/index.html')


def privacy_policy(request):
    return render(request, 'core/docs/privacy_policy.html')

def terms_of_service(request):
    return render(request, 'core/docs/terms_of_service.html')