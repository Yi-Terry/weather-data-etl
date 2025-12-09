import requests

api_url = "https://api.weatherstack.com/current?access_key=d8e00dc29d246a3bb80084cc1a3aee44&query=New York"
def fetch_data():
    resopnse = request.get(api_url)
    print(resopnse)