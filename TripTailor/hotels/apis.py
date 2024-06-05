# import requests

# # Replace these with your actual API keys
# BOOKING_API_KEY = '"073b84173amsh6d9240ca601335bp1912fdjsn2738ab12f212",'
# BOOKING_API_HOST = 'https://booking-com15.p.rapidapi.com'

# def fetch_hotels(search_params):
#     url = f"{BOOKING_API_HOST}/api/v1/hotels/getHotelDetails"
#     headers = {
#         "X-RapidAPI-Key": BOOKING_API_KEY,
#         "X-RapidAPI-Host": "booking-com15.p.rapidapi.com",
#     }

#     required_params = [
#         "hotel_id",
#         "arrival_date",
#         "departure_date",
#     ]

#     for param in required_params:
#         if param not in search_params:
#             raise ValueError(f"Missing required parameter: {param}")

#     querystring = {
#         "hotel_id": search_params["hotel_id"],
#         "arrival_date": search_params["arrival_date"],
#         "departure_date": search_params["departure_date"],
#         "adults": search_params.get("adults", 1),
#         "children_age": search_params.get("children_age", ""),
#         "room_qty": search_params.get("room_qty", 1),
#         "units": search_params.get("units", "metric"),
#         "temperature_unit": search_params.get("temperature_unit", "c"),
#         "languagecode": search_params.get("languagecode", "en-us"),
#         "currency_code": search_params.get("currency_code", "EUR"),
#     }

#     response = requests.get(url, headers=headers, params=querystring)
#     response.raise_for_status()  # Raise an exception for non-2xx status codes

#     return response.json()