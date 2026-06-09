from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from .forms import UserProfileForm


# Create your views here.
@login_required
def profile(request):
    """Show and update the user's profile"""
    profile = get_object_or_404(UserProfile, user=request.user)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile, user=request.user)
        if form.is_valid():
            form.save()
            request.user.username = form.cleaned_data['username']
            request.user.first_name = form.cleaned_data['first_name']
            request.user.last_name = form.cleaned_data['last_name']
            request.user.email = form.cleaned_data['email']
            request.user.save()
            messages.success(request, "Profile updated successfully!")
        else:
            messages.error(
                request, "Update failed. Please ensure the form is valid."
                )
    else:
        form = UserProfileForm(instance=profile, user=request.user)

    orders = []

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'profile': profile,
        'orders': orders,
    }
    return render(request, template, context)


@login_required
def delete_profile(request):
    """this function is to allow the user to delete thir account"""
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
