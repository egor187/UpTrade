from django.shortcuts import render


def index(request):
    return render(request, 'TreeMenu/base.html', context={})
