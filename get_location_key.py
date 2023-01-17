import requests
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.environ.get("api_key")
location = os.environ.get("location")

url = f"http://dataservice.accuweather.com/locations/v1/cities/search?apikey={api_key}&q={location}"
response = requests.get(url)
data = response.json()
simpendata = open("location.txt", "w")
simpendata.write(str(data))
simpendata.close()
