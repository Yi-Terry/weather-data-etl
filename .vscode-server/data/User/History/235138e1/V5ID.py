import requests

api_url = "https://api.weatherstack.com/current?access_key = YOUR_ACCESS_KEY&query = New York"
def fetch_data():
    resopnse = request.get(api_url)
    print(resopnse)