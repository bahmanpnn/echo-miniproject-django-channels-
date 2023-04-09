from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'eecho/index.html')


def echo_image(request):
    return render(request, 'eecho/eecho_image.html')
