from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegisterForm(UserCreationForm):
    """
    A form for creating new users, including all the required fields,
    plus a repeated password.

    Attributes:
        email (EmailField): The email field for the form.
    """
    email = forms.EmailField()

    class Meta:
        """
        Metadata options for the UserRegisterForm.

        Attributes:
            model (Model): The model associated with this form.
            fields (list): The fields to include in the form.
        """
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    """
    A form for updating existing users,
    including the username and email fields.

    Attributes:
        email (EmailField): The email field for the form.
    """
    email = forms.EmailField()

    class Meta:
        """
        Metadata options for the UserUpdateForm.

        Attributes:
            model (Model): The model associated with this form.
            fields (list): The fields to include in the form.
        """
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    """
    A form for updating the user's profile,
    including the profile image.

    This form allows users to update their profile image.

    Attributes:
        No additional attributes outside of the Meta class.
    """
    class Meta:
        """
        Metadata options for the ProfileUpdateForm.

        Attributes:
            model (Model): The model associated with this form.
            fields (list): The fields to include in the form.
        """
        model = Profile
        fields = ['image']
