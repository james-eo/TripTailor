from django.db import models
from django.contrib.auth.models import User


class Country(models.Model):
    """
    Represents a country.

    Attributes:
        name (str): The name of the country.
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        """
        Returns the string representation of the Country.

        Returns:
            str: The name of the country.
        """
        return self.name


class Region(models.Model):
    """
    Represents a region within a country.

    Attributes:
        name (str): The name of the region.
        country (ForeignKey): Foreign key to the Country model.
    """
    name = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        """
        Returns the string representation of the Region.

        Returns:
            str: The name of the region.
        """
        return self.name


class City(models.Model):
    """
    Represents a city within a region.

    Attributes:
        name (str): The name of the city.
        region (ForeignKey): Foreign key to the Region model.
    """
    name = models.CharField(max_length=100)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

    def __str__(self):
        """
        Returns the string representation of the City.

        Returns:
            str: The name of the city.
        """
        return self.name


class Hotel(models.Model):
    """
    Represents a hotel.

    Attributes:
        name (str): The name of the hotel.
        country (ForeignKey): Foreign key to the Country model.
        city (ForeignKey): Foreign key to the City model, nullable.
        region (ForeignKey): Foreign key to the Region model.
        description (str): A detailed description of the hotel.
        amenities (str): A list of amenities offered by the hotel.
        price (Decimal): The price per night.
        currency (str): The currency of the price.
        rating (float): The rating of the hotel.
        address (str): The address of the hotel, nullable.
        attractions (str): Nearby attractions, nullable.
        facilities (str): Facilities available at the hotel, nullable.
        phone_number (str): The contact phone number, nullable.
        hotel_url (URLField): The website URL of the hotel, nullable.
        image_url (URLField): The image URL of the hotel, nullable.
        latitude (float): The latitude of the hotel location, nullable.
        longitude (float): The longitude of the hotel location, nullable.
    """
    name = models.CharField(max_length=200)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE, null=True)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    description = models.TextField()
    amenities = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3, default="USD")
    rating = models.FloatField()
    address = models.TextField(blank=True, null=True)
    attractions = models.TextField(blank=True, null=True)
    facilities = models.TextField(blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    hotel_url = models.URLField(blank=True, null=True)
    image_url = models.URLField(blank=True, null=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)

    def __str__(self):
        """
        Returns the string representation of the Hotel.

        Returns:
            str: The name of the hotel.
        """
        return self.name


class HotelImage(models.Model):
    """
    Represents an image of a hotel.

    Attributes:
        hotel (ForeignKey): Foreign key to the Hotel model.
        image_url (URLField): The URL of the image.
    """
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    image_url = models.URLField(blank=True)
