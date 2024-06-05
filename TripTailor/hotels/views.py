from django.shortcuts import render
from . models import Hotel, Country, City, Region
import requests
from django.shortcuts import render, get_object_or_404



def home(request):
    """Render the home page with a search form."""
    carousel1_images = ["hotels/image/paris.jpg", "hotels/image/london.jpg", "hotels/image/lagos.jpg"]
    carousel2_buttons = ["All", "Most popular", "Trending", "New location"]
    carousel2_images = ["hotels/image/paris.jpg", "hotels/image/london.jpg", "hotels/image/lagos.jpg"]
    carousel3_images = ["hotels/image/paris.jpg", "hotels/image/london.jpg", "hotels/image/lagos.jpg"]

    context = {
        "carousel1_images": carousel1_images,
        "carousel2_buttons": carousel2_buttons,
        "carousel2_images": carousel2_images,
        "carousel3_images": carousel3_images,
    }
    
    return render(request, 'hotels/home.html', context)


def about(request):
    return render(request, 'hotels/about.html')

def accommodations(request):
    context = {
        'hotel_list': Hotel.objects.all()
    }
    return render(request, 'hotels/accommodations.html', context)



def search_results(request):
    """
    Handle search form submission and display filtered
    hotel recommendations based on user criteria.
    """
    # Retrieve user input from the form 
    country = request.GET.get('country')
    city = request.GET.get('city')
    lodge_type = request.GET.get('lodge_type')
    budget = request.GET.get('budget')

    # Use APIs to retrieve locations and hotel data (replace with your actual API calls)
    countries_url = "https://api.example.com/countries"
    hotels_url = "https://api.example.com/hotels"

    # Get all countries
    response = requests.get(countries_url)
    countries = response.json()  # Assuming the API returns JSON data

    # Get hotels based on user criteria (if country or city is selected)
    hotels = []
    if country or city:
        params = {
            'country': country,
            'city': city,
        }
    response = requests.get(hotels_url, params=params)
    hotels = response.json()
    # Filter hotels by hotel type (if provided)
    if lodge_type:
        hotels = [hotel for hotel in hotels if hotel['type'] == lodge_type]

    # Filter hotels by budget range
    if budget:
        # Parse the budget range (assuming format like "$50 - $100")
        min_price, max_price = budget.split(" - ")
        hotels = [hotel for hotel in hotels if int(hotel['price']) >= int(min_price) and int(hotel['price']) <= int(max_price)]

    # Group hotels by price range
    price_ranges = {}
    for hotel in hotels:
        price_range = get_price_range(hotel['price'])
        if price_range not in price_ranges:
            price_ranges[price_range] = []
        price_ranges[price_range].append(hotel)

    context = {
        'countries': countries,
        'city_options': [],  # Will be populated dynamically based on selected country
        'hotels': hotels,  # List of all filtered hotels (for initial display)
        'price_ranges': price_ranges,
        'selected_country': country,
        'selected_city': city,
        'selected_hotel_type': lodge_type,
        'selected_budget': budget,
    }

    return render(request, 'hotels/search_results.html', context)


def get_price_range(price, currency):
    """
    This function defines the logic for grouping hotels by price range, 
    considering the hotel's currency.

    Args:
        price: The hotel's price as a decimal value.
        currency: The hotel's currency code (e.g., USD, EUR).

    Returns:
        A string representing the price range with the hotel's currency symbol.
    """
    price_int = int(price)
    if price_int <= 100:
        return f"{price_int} {currency} - {100} {currency}"
    elif price_int <= 200:
        return f"{100} {currency} - {200} {currency}"
    else:
        return f"{200} {currency}+"


def hotel_details(request, hotel_id):
    """
    Redirect the user to the hotel booking site using the hotel ID.
    """
    # Retrieve hotel details based on hotel ID using your hotel API
    hotels_url = "https://api.example.com/hotels/" + str(hotel_id)  # Replace with your hotel API endpoint
    response = requests.get(hotels_url)
    hotel_data = response.json()

    if hotel_data:  # Check if hotel data is retrieved successfully
        booking_url = hotel_data.get('booking_url')  # Assuming 'booking_url' field exists
        if booking_url:
            return render(request, 'hotels/hotel_details.html', {'booking_url': booking_url})
        else:
            # Handle case where booking URL is not available in the response
            context = {'error_message': 'Booking URL not available for this hotel.'}
            return render(request, 'hotels/hotel_details.html', context)
    else:
        # Handle case where hotel data retrieval fails
        context = {'error_message': 'Hotel details not found.'}
        return render(request, 'hotels/hotel_details.html', context)