import requests
from django.http import JsonResponse

def find_movies(request):
    url = "https://api.themoviedb.org/3/discover/movie"

    headers = {
        "Accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIxZmE5N2M3MmRiMzc5ZWQ3NTI1YjQzOWFkNDUyOTVkZSIsIm5iZiI6MTczODE0NDgwNS4zMzksInN1YiI6IjY3OTlmYzI1YjRiNmY5MTQ1M2E5Nzg5NiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.yLFDBI3XXf7qaHKor1cgTl2ngAzz4trzs63gvNN__Sg",
    }

    # Get 'page' from URL, default to 1
    page = request.GET.get("page", "1")
    if not page.isdigit():
        return JsonResponse({'error': "Invalid page number"}, status=400)

    params = {
        "include_adult": "false",
        "include_video": "false",
        "language": "en-US",
        "page": int(page),
        "sort_by": "popularity.desc",
        "with_genres": 35,  # Comedy Genre
    }

    try:
        response = requests.get(url, params=params, headers=headers, timeout=10)

        # ✅ Fix: Return the exact error code instead of always using 500
        if response.status_code != 200:
            return JsonResponse({'error': f"Failed to fetch data: {response.status_code}"}, status=response.status_code)

        data = response.json()

        # ✅ Fix: Ensure API response contains 'results'
        if not isinstance(data, dict) or "results" not in data:
            return JsonResponse({'error': "Unexpected response format"}, status=500)

        # ✅ Fix: Prevent errors if 'total_results' is missing
        total_results = data.get("total_results", len(data["results"]))

        # ✅ Extract only useful movie details
        movies = [
            {
                "title": movie.get("title"),
                "release_date": movie.get("release_date"),
                "overview": movie.get("overview"),
                "popularity": movie.get("popularity"),
                "poster": f"https://image.tmdb.org/t/p/w500{movie.get('poster_path')}" if movie.get("poster_path") else None,
                "vote_average": movie.get("vote_average"),
                "vote_count": movie.get("vote_count"),
            }
            for movie in data["results"]
        ]

        return JsonResponse({"movies": movies, "total_results": total_results, "page": int(page)}, safe=False)

    except requests.exceptions.RequestException as e:
        return JsonResponse({"error": f"Request failed: {str(e)}"}, status=500)
