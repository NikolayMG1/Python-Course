import sys
import json
import requests
from requests.exceptions import HTTPError
API_KEY = '09590459f97f24cb86cf1072598488ca'
import Read_input
import Read_output
import Read_trending
import asyncio

async def my_f(a1,a2,a3):
    # a1,a2,a3 = Read_input.read_input()
    read_trends = Read_trending.read_trending(a1,a2)
    Read_output.read_output(a1,a2,a3, read_trends)



async def main():
    input = [['movie', 'week', 'csv'], ['movie', 'day', 'csv'],
         ['tv', 'week', 'csv'], ['movie', 'day', 'csv'],   
         ['movie', 'week', 'json'], ['movie', 'day', 'json'],
         ['tv', 'week', 'json'], ['movie', 'day', 'json']]

    coroutines = [my_f(item[0],item[1],item[2]) for item in input]
    results = await asyncio.gather(*coroutines)
    print(results)

if __name__ == "__main__":
    asyncio.run(main())