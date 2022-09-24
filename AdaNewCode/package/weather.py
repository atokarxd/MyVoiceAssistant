import requests
from engine import Engine

class Weather:
    def __init__(self) -> None:
        res = requests.get('https://ipinfo.io/')
        data = res.json()
        city = data['city']
        url = 'http://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=e4a09f04b4d5d074c9ecd71a71d7e1c4&lang=en'
        self.motor = Engine()
        api_link = requests.get(url)
        self.api_data = api_link.json()

    def weather(self):
        if self.api_data['cod'] == '404':
            self.motor.Output("You're not connected to the Internet.")
        else:
            temperature = int(((self.api_data['main']['temp']) - 273.15))
            weather_script = self.api_data['weather'][0]['description']
            humidity = self.api_data['main']['humidity']
            wind = self.api_data['wind']['speed']

        data = f'Temperature: {temperature} celsius degrees.\nWeather outside, {weather_script}.\nHumidity: {int(humidity)} %.\nWind: {int(wind)} km/h.'
        self.motor.Output(data)
        return data