import requests
api_key = "d8e00dc29d246a3bb80084cc1a3aee44"
api_url = f"https://api.weatherstack.com/current?access_key={api_key}&query=New York"
def fetch_data():
    print("Fetching weather data from Weatherstack API...")
    try:
    
        response = requests.get(api_url)
        response.raise_for_status()
        print("API response recieved success")
        return response.json()

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        raise
fetch_data()

def mock_fetch_data():
        return {'request': {'type': 'City', 'query': 'New York, United States of America', 'language': 'en', 'unit': 'm'}, 'location': {'name': 'New York', 'country': 'United States of America', 'region': 'New York', 'lat': '40.714', 'lon': '-74.006', 'timezone_id': 'America/New_York', 'localtime': '2025-12-04 20:36', 'localtime_epoch': 1764880560, 'utc_offset': '-5.0'}, 'current': {'observation_time': '01:36 AM', 'temperature': -1, 'weather_code': 113, 'weather_icons': ['https://cdn.worldweatheronline.com/images/wsymbols01_png_64/wsymbol_0008_clear_sky_night.png'], 'weather_descriptions': ['Clear '], 'astro': {'sunrise': '07:04 AM', 'sunset': '04:28 PM', 'moonrise': '03:54 PM', 'moonset': '06:53 AM', 'moon_phase': 'Full Moon', 'moon_illumination': 98}, 'air_quality': {'co': '165.85', 'no2': '10.45', 'o3': '71', 'so2': '3.15', 'pm2_5': '3.45', 'pm10': '3.55', 'us-epa-index': '1', 'gb-defra-index': '1'}, 'wind_speed': 27, 'wind_degree': 321, 'wind_dir': 'NW', 'pressure': 1024, 'precip': 0, 'humidity': 41, 'cloudcover': 0, 'feelslike': -8, 'uv_index': 0, 'visibility': 16, 'is_day': 'no'}}