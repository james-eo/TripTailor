from django.shortcuts import render
from django.http import JsonResponse
from .models import Hotel, Country, City, Region

def home(request):
    """Render the home page with a search form."""
    countries = Country.objects.all()
    context = {
        'countries': countries,
    }
    return render(request, 'hotels/home.html', context)

def get_regions(request, country_id):
    regions = Region.objects.filter(country_id=country_id)
    regions_list = list(regions.values('id', 'name'))
    return JsonResponse(regions_list, safe=False)

def get_cities(request, region_id):
    cities = City.objects.filter(region_id=region_id)
    cities_list = list(cities.values('id', 'name'))
    return JsonResponse(cities_list, safe=False)

def accommodations(request):
    """Handle the display of hotels and search results."""
    countries = Country.objects.all()
    context = {
        'countries': countries,
    }
    
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

    context = {
        'hotel_list': hotels,
    }
    return render(request, 'hotels/accommodations.html', context)


def about(request):
    return render(request, 'hotels/about.html')