# import json
#
# def weather_api_fetch():
#     file_path = r"D:\new\weather.json"  #r iis row string
#
#     with open(file_path, "r") as file:  #open file in read mode
#         data = json.load(file) #convert in json file
#
#     if data.get("data"):
#         timezone = data["timezone"]
#         temperature = data["data"][0]["temp"]
#         return timezone, temperature
#     else:
#         raise Exception("Something went wrong")
#
#
# def main():
#     try:
#         timezone, temperature = weather_api_fetch()
#         print(f"The temperature is {temperature} degrees celsius and the timezone is {timezone}")
#     except Exception as e:
#         print(e)
#
# if __name__ == "__main__":
#     main()




import requests
import json
from datetime import datetime


cities = [
    {"name": "London", "lat": 51.5072, "lon": -0.1276},
    {"name": "New York", "lat": 40.7128, "lon": -74.0060},
    {"name": "Tokyo", "lat": 35.6762, "lon": 139.6503},
    {"name": "Paris", "lat": 48.8566, "lon": 2.3522},
    {"name": "Sydney", "lat": -33.8688, "lon": 151.2093},
    {"name": "Dubai", "lat": 25.276987, "lon": 55.296249},
    {"name": "Singapore", "lat": 1.3521, "lon": 103.8198},
    {"name": "Toronto", "lat": 43.65107, "lon": -79.347015},
    {"name": "Mumbai", "lat": 19.0760, "lon": 72.8777},
    {"name": "Cape Town", "lat": -33.9249, "lon": 18.4241},
    {"name": "Surat", "lat": 21.1744 , "lon": 72.8243},
]

weather_data = {"fetched_at": datetime.now().isoformat(), "cities": []}

# Fetch weather for each city
for city in cities:
    url = f"https://api.open-meteo.com/v1/forecast?latitude={city['lat']}&longitude={city['lon']}&current_weather=true"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json().get("current_weather", {})
        # print(f"\n🔍 Raw API response for {city['name']}:")
        # print(json.dumps(data))
        city_weather = {
            "city": city["name"],
            "temperature": data.get("temperature"),
            "windspeed": data.get("windspeed"),
            "winddirection": data.get("winddirection"),
            "weathercode": data.get("weathercode"),
            "time": data.get("time"),
        }
        weather_data["cities"].append(city_weather)
    else:
        print(f"⚠ Failed to fetch data for {city['name']}")

# Save data to JSON file
with open("weather_data.json", "w") as f:
    json.dump(weather_data, f, indent=4)

print("✅ Weather data saved to 'weather_data.json'")

# --- Part 2: Get city data from input ---
city_name = input("\nEnter a city name to view its weather: ").strip().title()   #strip l&r space remove

with open("weather_data.json", "r") as f:
    data = json.load(f)

found_city = next((c for c in data["cities"] if c["city"] == city_name), None)

if found_city:
    print(f"\n🌤 Weather in {found_city['city']}:")
    print(f"🌡 Temperature: {found_city['temperature']}°C")
    print(f"💨 Windspeed: {found_city['windspeed']} km/h")
    print(f"🧭 Wind Direction: {found_city['winddirection']}°")
    print(f"🕒 Time: {found_city['time']}")
else:
    print("❌ City not found in stored data.")