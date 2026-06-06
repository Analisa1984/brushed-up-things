from django.shortcuts import render
from .models import Artwork


# Create your views here.
def index(request):
    return render(request, 'index.html')


def gallery(request):
    artworks = Artwork.objects.filter(is_sold=False).order_by('-created_at')
    template = 'artwork/gallery.html'
    context = {'artworks': artworks}
    return render(request, template, context)
