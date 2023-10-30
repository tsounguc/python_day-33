import requests
from datetime import datetime

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# print(response)

# Different Responses
# 1XX: Hold on
# 2XX: Here You Go
# 3XX: Go away
# 4XX: You Screwed up
# 5XX: Server Screwed up

# response.raise_for_status()
# data = response.json()
#
#
# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]
#
# iss_position = (longitude, latitude)
#
# print(iss_position)

parameters = {
    "lat": 38.907192,
    "lng": -77.036873,
    "formatted": 0
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

print(sunrise)
print(sunset)

time_now = datetime.now()


