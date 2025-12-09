import requests
api_key = "d8e00dc29d246a3bb80084cc1a3aee44"
api_url = f"https://api.weatherstack.com/current?access_key={api_key}&query=New York"
def fetch_data():
    try:
        
        response = requests.get(api_url)
        response.raise_for_status()
        print("API response recieved success")
        return response.json()

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        raise
fetch_data()