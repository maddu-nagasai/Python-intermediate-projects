import requests

API_KEY = "8e21347b8d203d9c22c31e138543b9cc"  # Replace with your API key
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    """Fetches weather data from OpenWeather API."""
    params = {"q": city, "appid": API_KEY, "units": "metric"}
    response = requests.get(BASE_URL, params=params)
    
    if response.status_code == 200:
        data = response.json()
        weather = data["weather"][0]["description"].capitalize()
        temp = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]
        
        print(f"\n🌍 Weather in {city.capitalize()}:")
        print(f"🌤 Condition: {weather}")
        print(f"🌡 Temperature: {temp}°C (Feels like {feels_like}°C)")
        print(f"💧 Humidity: {humidity}%")
        print(f"💨 Wind Speed: {wind_speed} m/s")
    else:
        print("❌ Error fetching weather. Check city name or API key.")

def main():
    print("\n⛅ Real-Time Weather App ⛅")
    
    while True:
        city = input("\nEnter city name (or 'exit' to stop): ").strip()
        if city.lower() == "exit":
            print("Goodbye! ☀️")
            break
        get_weather(city)

if __name__ == "__main__":
    main()
