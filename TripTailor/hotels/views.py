from django.shortcuts import render
from django.http import JsonResponse
from .models import Hotel, Country, City, Region


def home(request):
    """
    Render the home page with a search form.

    This view fetches all countries from the database and passes them to the
    'hotels/home.html' template for rendering.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: Rendered home page with countries list.
    """
    countries = Country.objects.all()
    context = {
        'countries': countries,
    }
    return render(request, 'hotels/home.html', context)


def get_regions(request, country_id):
    """
    Return regions for a given country as a JSON response.

    This view fetches regions related to the provided country ID and returns
    them in JSON format.

    Args:
        request: The HTTP request object.
        country_id (int): The ID of the country to fetch regions for.

    Returns:
        JsonResponse: List of regions in JSON format.
    """
    regions = Region.objects.filter(country_id=country_id)
    regions_list = list(regions.values('id', 'name'))
    return JsonResponse(regions_list, safe=False)


def get_cities(request, region_id):
    """
    Return cities for a given region as a JSON response.

    This view fetches cities related to the provided region ID and returns
    them in JSON format.

    Args:
        request: The HTTP request object.
        region_id (int): The ID of the region to fetch cities for.

    Returns:
        JsonResponse: List of cities in JSON format.
    """
    cities = City.objects.filter(region_id=region_id)
    cities_list = list(cities.values('id', 'name'))
    return JsonResponse(cities_list, safe=False)


def accommodations(request):
    """
    Handle the display of hotels and search results.

    This view fetches and filters hotels based on provided query parameters
    such as country, region, city, and budget. It then renders the
    'hotels/accommodations.html' template with the filtered hotel list.

    Args:
        request: The HTTP request object.

    Query Parameters:
        country (str): The ID of the country to filter hotels by.
        region (str): The ID of the region to filter hotels by.
        city (str): The ID of the city to filter hotels by.
        budget (str): The budget range to filter hotels by,
        in the format "min - max".

    Returns:
        HttpResponse: Rendered accommodations page with filtered hotel list.
    """
    country = request.GET.get('country')
    region = request.GET.get('region')
    city = request.GET.get('city')
    budget = request.GET.get('budget')

    hotels = Hotel.objects.all()

    if country:
        hotels = hotels.filter(country_id=country)
    if region:
        hotels = hotels.filter(region_id=region)
    if city:
        hotels = hotels.filter(city_id=city)
    if budget:
        min_price, max_price = map(int, budget.split(" - "))
        hotels = hotels.filter(price__gte=min_price, price__lte=max_price)

    countries = Country.objects.all()
    context = {
        'hotel_list': hotels,
        'countries': countries,
    }
    return render(request, 'hotels/accommodations.html', context)


def about(request):
    """
    Render the about page.

    This view renders the 'hotels/about.html' template.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: Rendered about page.
    """
    return render(request, 'hotels/about.html')
