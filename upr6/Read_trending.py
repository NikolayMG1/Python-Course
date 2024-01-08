import requests
from requests.exceptions import HTTPError
API_KEY = '09590459f97f24cb86cf1072598488ca'

def read_trending(media_type, time_window):
    try:
        url = f'https://api.themoviedb.org/3/trending/{media_type}/{time_window}?api_key={API_KEY}'
        # print(url)
        response = requests.get(url)
        response.raise_for_status()
        # print(response.json().get('results', []))
        return response.json().get('results', [])
    except requests.RequestException as e:
        print(f"Request failed: {e}")
        return None