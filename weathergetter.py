import requests


def get_status(zipcode):
    countrycode = "US"
    apikey = '3dad82ec0200d5e30cbdab1788cca74c'
    link = f"https://api.openweathermap.org/data/2.5/weather?zip={zipcode},{countrycode}&appid={apikey}"
    page = requests.get(link)
    x = page.json()
    weather = x['weather']
    if x['cod'] != "404":
        return weather[0]['main']
    else:
        return ("An error occurred.")


def get_description(zipcode):
    countrycode = "US"
    apikey = '3dad82ec0200d5e30cbdab1788cca74c'
    link = f"https://api.openweathermap.org/data/2.5/weather?zip={zipcode},{countrycode}&appid={apikey}"
    page = requests.get(link)
    x = page.json()
    weather = x['weather']
    if x['cod'] != "404":
        return weather[0]['description']
    else:
        return ("An error occurred.")

