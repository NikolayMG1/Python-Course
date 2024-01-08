import json
from requests.exceptions import HTTPError
API_KEY = '09590459f97f24cb86cf1072598488ca'
import Read_trending


def read_output(media_type, time_window, output_format, trending):
    
    formatted_data = [{'title': item['name' if media_type == 'tv' else 'title'], 'rating': item['vote_average']} for item in trending]

    try:
        if output_format == 'json':
            output_list = [{'title': item['title'], 'rating': item['rating']} for item in formatted_data]
            sorted_output = sorted(output_list, key=lambda x: x['rating'], reverse=True)
            output = json.dumps(sorted_output, indent=2)
            print(output)
            
        elif output_format == 'csv':
            sorted_data = sorted(formatted_data, key=lambda x: x['rating'], reverse=True)
            print("title,rating")
            for item in sorted_data:
                print(f"{item['title']},{item['rating']}")
    except (KeyError, IndexError) as e:
        print(f"Error formatting data: {e}")