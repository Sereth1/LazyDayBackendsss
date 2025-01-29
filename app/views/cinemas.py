import requests
from django.http import JsonResponse
import urllib.parse  

def find_cinemas(request):
    location = request.GET.get("location", ",")  

    
    location_parts = location.split(",")  
    city = location_parts[0].strip() if len(location_parts) > 0 else ""
    country = location_parts[1].strip() if len(location_parts) > 1 else ""

    url = "https://nominatim.openstreetmap.org/search"
    params = {
        "q": f"cinema in {city}, {country}",  
        "format": "json",
        "limit": 10,
        "addressdetails": 1,
        "extratags": 1
    }
    headers = {
        "User-Agent": "LazySundayApp/1.0 (contact@example.com)"  
    }

    try:
        response = requests.get(url, params=params, headers=headers, timeout=5)

        if response.status_code != 200:
            return JsonResponse({"error": f"Failed to fetch data: {response.status_code}"}, status=500)

        data = response.json()

        if not isinstance(data, list):
            return JsonResponse({"error": "Unexpected response format"}, status=500)

        cinemas = [
            {
                "name": place.get("display_name", "Unknown Cinema"),
                "latitude": place.get("lat"),
                "longitude": place.get("lon"),
                "address": place.get("address", {}),
                "city": place.get("address", {}).get("city", "Unknown"),
                "country": place.get("address", {}).get("country", "Unknown"),
                "website": place.get("extratags", {}).get("website", "N/A"),
                "phone": place.get("extratags", {}).get("phone", "N/A"),
            }
            for place in data
        ]

        return JsonResponse(cinemas, safe=False)

    except requests.exceptions.RequestException as e:
        return JsonResponse({"error": f"Request failed: {str(e)}"}, status=500)
