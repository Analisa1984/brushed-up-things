from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import UserProfile
from .forms import UserProfileForm, ArtistForm, ArtworkForm
from artwork.models import Artist, Artwork


def is_staff_check(user):
    return user.is_authenticated and user.is_staff


@user_passes_test(is_staff_check)
def staff_dashboard(request):
    """Display staff portal"""
    artworks = Artwork.objects.all()
    artists = Artist.objects.all()

    template = 'profiles/staff_dashboard.html'
    context = {
        'artworks': artworks,
        'artists': artists,
    }
    return render(request, template, context)


@login_required
def profile(request):
    """Show and update the user's profile"""
    profile = get_object_or_404(UserProfile, user=request.user)
    if request.method == 'POST':
        form = UserProfileForm(
            request.POST, instance=profile, user=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully!")
        else:
            messages.error(
                request, "Update failed. Please ensure the form is valid."
            )
    else:
        form = UserProfileForm(instance=profile, user=request.user)

    # get real transaction history from checkout app
    orders = profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'profile': profile,
        'orders': orders,
    }
    return render(request, template, context)


@login_required
def delete_profile(request):
    """This function is to allow the user to delete their account"""
    if request.method == 'POST':
        user = request.user
        logout(request)
        user.delete()
        messages.success(
            request,
            "Your account has been deleted. "
            "Our team at Brushed up Things is sorry to see you go. "
            "If you have any feedback on how we can improve,"
            " please don't hesitate to reach out. "
            "We hope to welcome you back in the future!"
        )
        return redirect('index')
    return redirect('profile')


@user_passes_test(is_staff_check)
def add_artist(request):
    """View for staff members to add a new artist to the gallery"""
    if request.method == 'POST':
        form = ArtistForm(request.POST, request.FILES)
        if form.is_valid():
            artist = form.save()
            messages.success(request, f'Successfully added artist: {
                artist.name
                }'
                )
            return redirect('staff_dashboard')
        else:
            messages.error(
                request,
                'Failed to add artist. Please ensure the form is valid.'
            )
    else:
        form = ArtistForm()

    template = 'profiles/add_artist.html'
    context = {
        'form': form,
    }
    return render(request, template, context)


@user_passes_test(is_staff_check)
def add_artwork(request):
    """View for staff members to add a new piece of artwork"""
    if request.method == 'POST':
        form = ArtworkForm(request.POST, request.FILES)
        if form.is_valid():
            artwork = form.save()
            messages.success(
                request, f'Successfully added artwork: {artwork.title}')
            return redirect('staff_dashboard')
        else:
            messages.error(
                request,
                'Failed to add artwork. Please ensure the form is valid.')
    else:
        form = ArtworkForm()

    template = 'profiles/add_artwork.html'
    context = {
        'form': form,
    }
    return render(request, template, context)
