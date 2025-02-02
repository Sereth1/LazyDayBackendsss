import requests
from django.http import JsonResponse

def find_movies(request):
    url = "https://api.themoviedb.org/3/discover/movie"

    headers = {
        "Accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIxZmE5N2M3MmRiMzc5ZWQ3NTI1YjQzOWFkNDUyOTVkZSIsIm5iZiI6MTczODE0NDgwNS4zMzksInN1YiI6IjY3OTlmYzI1YjRiNmY5MTQ1M2E5Nzg5NiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.yLFDBI3XXf7qaHKor1cgTl2ngAzz4trzs63gvNN__Sg",
    }

    
    year = request.GET.get("year")
    pages_to_fetch = int(request.GET.get("pages", 5))  

    params = {
        "include_adult": "false",
        "include_video": "false",
        "language": "en-US",
        "sort_by": "popularity.desc",
        "with_genres": 35,  
    }

    if year and year.isdigit():
        params["primary_release_year"] = int(year)

    all_movies = []
    current_page = 1
    total_pages = 20

    try:
        while current_page <= total_pages and current_page <= pages_to_fetch:
            params["page"] = current_page
            response = requests.get(url, params=params, headers=headers, timeout=10)

            if response.status_code != 200:
                return JsonResponse({'error': f"Failed to fetch data: {response.status_code}"}, status=response.status_code)

            data = response.json()

            if not isinstance(data, dict) or "results" not in data:
                return JsonResponse({'error': "Unexpected response format"}, status=500)

            total_pages = data.get("total_pages", 1)  
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

            all_movies.extend(movies) 
            current_page += 1 

        return JsonResponse({"movies": all_movies, "total_results": len(all_movies)}, safe=False)

    except requests.exceptions.RequestException as e:
        return JsonResponse({"error": f"Request failed: {str(e)}"}, status=500)
