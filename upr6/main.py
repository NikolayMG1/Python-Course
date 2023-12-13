import sys
import json
import requests
from requests.exceptions import HTTPError
API_KEY = '09590459f97f24cb86cf1072598488ca'

class Read_output:
    
    def read_output(media_type, time_window, output_format):
        read_trends = Read_trending.read_trending(media_type, time_window)
        if not read_trends:
            print("Couldnt get info, bg")
            return
        trending = sorted(read_trends, key=lambda x: x.get('vote_average', 0), reverse=True)

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

class Read_trending:

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
        
class Read_input:
    
    def read_input():

        if len(sys.argv) != 4:
            print("INVALID NUMBER OF ARGUMENTS, BOOM BOOM!!!")
            return False
        
        media_type = sys.argv[1]
        time_window = sys.argv[2]
        output_format = sys.argv[3]

        try:
            if media_type not in ['tv', 'movie'] or time_window not in ['day', 'week'] or output_format not in ['csv', 'json']:
                print("invalid input")
            else:
                Read_output.read_output(media_type, time_window, output_format)

        except ValueError:   
            return False      
            
        
def main():
        Read_input.read_input()

if __name__ == "__main__":
    main()