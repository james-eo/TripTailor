from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import (UserRegisterForm,
                    UserUpdateForm,
                    ProfileUpdateForm
                    )

def register(request):
    """
    Handle user registration.

    This view handles the registration of a new user.
    If the request method is POST, it processes the
    submitted registration form. If the form is valid,
    it saves the new user, displays a success message,
    and redirects to the login page. If the request method is GET,
    it displays the empty registration form.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: Rendered registration page with the registration form.
    """
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request,
                f'Account created successfully! You are now able to login'
                             )
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

def logout_view(request):
    """
    Handle user logout.

    This view logs out the user and then renders the logout page. 

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: Rendered logout page.
    """
    logout(request)
    return render(request, 'users/logout.html')

@login_required
def profile(request):
    """
    Handle user profile update.

    This view allows logged-in users to update their profile information.
    If the request method is POST,
    it processes the submitted profile update form.
    If the forms are valid, it saves the changes,
    displays a success message, and redirects to the profile page. 
    If the request method is GET, it displays the profile update forms
    with the current user information.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: Rendered profile page
        with the profile update forms.
    """
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile
                                   )
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    
    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'users/profile.html', context)