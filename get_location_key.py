import requests
import os
import json
from dotenv import load_dotenv

load_dotenv()
api_key = os.environ.get("api_key")
location = os.environ.get("location")

# get location key
url = f"http://dataservice.accuweather.com/locations/v1/cities/search?apikey={api_key}&q={location}&details=false"
response = requests.get(url)
data = json.loads(response.text)

# sanitize response
sanitized_city = data[0]["LocalizedName"]
location_key = data[0]["Key"]

# output sanitized response
print(f"your location key: {location_key}, and your city according to response is {sanitized_city}")



