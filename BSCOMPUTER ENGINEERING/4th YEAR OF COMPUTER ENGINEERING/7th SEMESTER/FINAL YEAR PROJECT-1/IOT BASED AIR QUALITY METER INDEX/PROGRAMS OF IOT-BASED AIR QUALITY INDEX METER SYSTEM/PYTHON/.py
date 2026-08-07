import requests
API_KEY = '39QDt7fVWUuPqLsPDAF3XkuDQEKiZkxN9z'  # Replace with your OpenWeatherMap API key
URL = "http://api.openweathermap.org/data/2.5/air_pollution"

def fetch_global_data(lat, lon):
    """Fetch air quality data for a specific location."""
    params = {'lat': lat, 'lon': lon, 'appid': API_KEY}
    response = requests.get(URL, params=params)
    if response.status_code == 200:
        data = response.json()
        pm2_5 = data['list'][0]['components']['pm2_5']
        pm10 = data['list'][0]['components']['pm10']
        return pm2_5, pm10
    else:
        print(f"Error: {response.status_code}, {response.text}")
        return None, None

# Example: Fetch air quality data for New York City
pm2_5, pm10 = fetch_global_data(40.7128, -74.0060)
if pm2_5 is not None and pm10 is not None:
    print(f"PM2.5: {pm2_5}, PM10: {pm10}")
else:
    print("Failed to fetch air quality data.")
