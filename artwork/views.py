from django.shortcuts import render, redirect, get_object_or_404
from .models import Artwork, Artist
from profiles.forms import ArtistForm, ArtworkForm
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


@user_passes_test(is_staff_check, login_url='index')
def artwork_directory(request):
    """View for staff members to see and manage the full artwork inventory"""
    artworks = Artwork.objects.all().order_by('-created_at')
    template = 'artwork/artwork_directory.html'
    context = {
        'artworks': artworks,
    }
    return render(request, template, context)


@user_passes_test(is_staff_check, login_url='index')
def edit_artwork(request, artwork_id):
    """View for staff members to edit details of an existing piece of art"""
    artwork = get_object_or_404(Artwork, pk=artwork_id)

    if request.method == 'POST':
        # once save is clicked on the form
        form = ArtworkForm(request.POST, request.FILES, instance=artwork)
        if form.is_valid():
            form.save()
            messages.success(
                request, f'Successfully updated "{artwork.title}"!'
                )
            return redirect('artwork_directory')
    else:
        # no new changes and current inventory remains the same
        form = ArtworkForm(instance=artwork)

    template = 'artwork/edit_artwork.html'
    context = {
        'form': form,
        'artwork': artwork,
    }
    return render(request, template, context)


@user_passes_test(is_staff_check, login_url='index')
def delete_artwork(request, artwork_id):
    """View for staff members to permanently delete an artwork"""
    artwork = get_object_or_404(Artwork, pk=artwork_id)
    artwork.delete()
    messages.success(
        request, f'Successfully deleted "{artwork.title}" from inventory.'
        )
    return redirect('artwork_directory')
