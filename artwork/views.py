from django.shortcuts import render, redirect, get_object_or_404
from .models import Artwork, Artist
from profiles.forms import ArtistForm, ArtworkForm
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages
from django.db.models import Q
from .forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings


# Create your views here.
def is_staff_check(user):
    """Helper function to check if a user is staff """
    return user.is_authenticated and user.is_staff


def index(request):
    return render(request, 'index.html')


def about_view(request):
    return render(request, 'about.html')


def gallery(request):
    """This function is to display the art collections also with filters"""
    # filters all artworks and artists
    artworks = Artwork.objects.all()
    all_artists = Artist.objects.all().order_by('name')

    # code to allow search bar to work
    selected_medium = request.GET.get('medium')
    selected_artist_id = request.GET.get('artist')
    query = request.GET.get('q')

    if selected_medium:
        artworks = artworks.filter(medium__icontains=selected_medium)
    if selected_artist_id:
        artworks = artworks.filter(artist_id=selected_artist_id)

    if query:
        queries = (
            Q(title__icontains=query) |
            Q(description__icontains=query) |
            Q(medium__icontains=query)
        )
        artworks = artworks.filter(queries)

    # this code will get the requested items by the filter user wants
    selected_medium = request.GET.get('medium')
    selected_artist_id = request.GET.get('artist')

    if selected_medium:
        artworks = artworks.filter(medium__icontains=selected_medium)
    if selected_artist_id:
        artworks = artworks.filter(artist_id=selected_artist_id)

    template = 'artwork/gallery.html'
    context = {
        'artworks': artworks,
        'all_artists': all_artists,
        'current_medium': selected_medium,
        'current_artist': selected_artist_id,
        'search_term': query,
        }
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
            messages.success(
                request, f'Successfully updated artist: {artist.name}'
                )
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


def contact_view(request):
    """
    contact form with email.
    """
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():

            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            message_text = form.cleaned_data["message"]

            subject = f"New Gallery Inquiry from {name}"
            body = (
                f"You received a new message regarding Brushed Up Things:\n\n"
                f"From: {name} ({email})\n\n"
                f"Message:\n{message_text}"
            )

            send_mail(
                subject,
                body,
                settings.EMAIL_HOST_USER,
                [settings.EMAIL_HOST_USER],
            )

            messages.success(
                request,
                "Thank you! Your message has been sent "
                "to the Brushed Up Things team. "
                "We will get in touch soon!"
            )
            return redirect("/contact/")
    else:
        form = ContactForm()

    template = "contact.html"
    context = {
        "form": form
    }

    return render(request, template, context)
