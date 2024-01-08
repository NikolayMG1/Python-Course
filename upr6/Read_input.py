import Read_output
import sys
import json
import requests
from requests.exceptions import HTTPError
API_KEY = '09590459f97f24cb86cf1072598488ca'
import Read_trending

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
            return (media_type, time_window, output_format)

    except ValueError:   
        return False      