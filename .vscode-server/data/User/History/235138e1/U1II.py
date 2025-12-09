import requests

api_url = "https://api.weatherstack.com/current?access_key=d8e00dc29d246a3bb80084cc1a3aee44&query=New York"
def fetch_data():
    try:

    resopnse = requests.get(api_url)
    response.raise_for_status()
    print("API response recieved success")
    return resopnse.json()

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
fetch_data()