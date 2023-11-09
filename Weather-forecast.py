import requests

def get_weather_data(api_key, city):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"  # Get temperature in Celsius
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None

def main():
    api_key = "Enter API Key"
    city = input("Enter the city name: ")

    weather_data = get_weather_data(api_key, city)

    if weather_data:
        temperature = weather_data["main"]["temp"]
        weather_desc = weather_data["weather"][0]["description"]
        humidity = weather_data["main"]["humidity"]
        wind_speed = weather_data["wind"]["speed"]

        print("Weather in", city)
        print("Temperature:", temperature, "°C")
        print("Description:", weather_desc)
        print("Humidity:", humidity, "%")
        print("Wind speed:", wind_speed, "km/h")
    else:
        print("City not found or an error occurred. Please check the city name and your API key.")

if __name__ == "__main__":
    main()
