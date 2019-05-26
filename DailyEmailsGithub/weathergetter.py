import pyowm, requests, json


def get_temperature(zipcode):
    owm = pyowm.OWM('3dad82ec0200d5e30cbdab1788cca74c')
    observation = owm.weather_at_place(zipcode)
    w = observation.get_weather()
    temperature = w.getTemperature()
    return temperature[1]


def get_status(zipcode, countrycode="US"):
    api_key = '3dad82ec0200d5e30cbdab1788cca74c'
    link = f"https://api.openweathermap.org/data/2.5/weather?appid={apikey}zip={zipcode},{countrycode}"
    page = requests.get(link)
    x = page.json()
    dictionary = dict(page.json())
    if dictionary["cod"] != "404":
        return dictionary["main"]


def get_description(zipcode, countrycode="US"):
    apikey = '3dad82ec0200d5e30cbdab1788cca74c'
    link = f"https://api.openweathermap.org/data/2.5/weather?appid={apikey}zip={zipcode},{countrycode}"
    page = requests.get(link)
    x = page.json()
    dictionary = dict(page.json())
    print(dictionary)
    if dictionary["cod"] != "404":
        return dictionary["description"]

# Today's weather is expected to be {get_status(area)}. The expected temperature for today is {get_temperature(
# area)} degrees fahrenheit. Have a wonderful day!###
