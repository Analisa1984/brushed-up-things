from django.shortcuts import render, redirect, get_object_or_404
from .models import Artwork, Artist
from profiles.forms import ArtistForm
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages


# Create your views here.
def is_staff_check(user):
    """Helper function to check if a user is staff """
    return user.is_authenticated and user.is_staff


def index(request):
    return render(request, 'index.html')


def gallery(request):
    artworks = Artwork.objects.filter(is_sold=False).order_by('-created_at')
    template = 'artwork/gallery.html'
    context = {'artworks': artworks}
    return render(request, template, context)


def artist_directory(request):
    """This shows all artists"""
    artists = Artist.objects.all()
    template = 'artwork/artist_directory.html'
    context = {
        'artists': artists,
    }
    return render(request, template, context)


@user_passes_test(is_staff_check, login_url='index')
def edit_artist(request, artist_id):
    """Edit an existing artist"""
    artist = get_object_or_404(Artist, pk=artist_id)
    if request.method == 'POST':
        form = ArtistForm(request.POST, request.FILES, instance=artist)
        if form.is_valid():
            form.save()
            return redirect('artist_directory')
        else:
            form = ArtistForm(instance=artist)
        template = 'artwork/edit_artist.html'
        context = {
            'form': form,
            'artist': artist,
        }
        return render(request, template, context)


@user_passes_test(is_staff_check, login_url='index')
def delete_artist(request, artist_id):
    """Delete an Artist from the list"""
    artist = get_object_or_404(Artist, pk=artist_id)
    artist.delete()
    return redirect('artist_directory')
