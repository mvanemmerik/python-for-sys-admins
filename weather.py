import os
import requests
import sys
from argparse  import ArgumentParser
import json

parser  =  ArgumentParser(description='Get the current weather for your zipcode')
parser.add_argument('zip', help='zip to get weather')
parser.add_argument('--country', default='us', help='"us" is default country')

args  = parser.parse_args()

api_key = os.getenv("OWM_API_KEY")

if not api_key:
    print("Error: no Open Weather Map API key 'OWM_API_KEY' provided")
    sys.exit(1)

url =  f"http://api.openweathermap.org/data/2.5/weather?zip={args.zip},{args.country}&appid={api_key}"

res = requests.get(url)

if res.status_code != 200:
    print(f"Error connecting to weather provider: {res.status_code}")
    sys.exit(1)

# print(res.json())
print(json.dumps(res.json(), indent=4, sort_keys=True))


