import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
# print(response)

# Different Responses
# 1XX: Hold on
# 2XX: Here You Go
# 3XX: Go away
# 4XX: You Screwed up
# 5XX: Server Screwed up

response.raise_for_status()
data = response.json()


longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]

iss_position = (longitude, latitude)

print(iss_position)