import requests
import sys


def weather(city_name):
    headers = {
        "X-RapidAPI-Key": "36d9867717msh152a633d26299dep192786jsnf80ec7e2e717",
        "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com",
    }
    base_url = "https://weatherapi-com.p.rapidapi.com/current.json"

    params = {"q": city_name}

    response = requests.get(base_url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        celsius_temp = data.get("current", {}).get("temp_c")
        if celsius_temp is not None:
            print(f"Temperature in {city_name.capitalize()}: {celsius_temp}°C")
            return 200
    print("Temperature data not available.")
    return 404


# Check if a city name argument is provided
if len(sys.argv) < 2:
    print("Please provide a city name as an argument.")
    sys.exit(1)

city_input = sys.argv[1]  # Get the city name from command-line arguments
result = weather(city_input)
print(result)
