from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    """
    Represents a user profile, which extends the built-in User model
    with additional fields.

    Attributes:
        user (OneToOneField): A one-to-one relationship
        with the User model.
        image (ImageField): The profile image of the user,
        with a default image.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        """
        Returns the string representation of the Profile.

        Returns:
            str: The username followed by 'Profile'.
        """
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        """
        Override the save method to resize the profile image
        if it is larger than 300x300 pixels.

        This method resizes profile image to a maximum of
        300x300 pixels to optimize storage and loading times.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
