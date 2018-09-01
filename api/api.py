from flask import Flask
from flask_restful import Resource, Api
import os
import requests
from .db import *

API_KEY = os.environ.get('API_KEY', None)

app = Flask(__name__)
api = Api(app)

class WeatherID(Resource):
    def get(self):
        try:
            url = 'https://api.openweathermap.org/data/2.5/weather?q=Jeju,KR&appid=' + API_KEY
            response = requests.get(url)

        except Exception as e:
            return {'error': str(e)}
        else:
            return response.text


api.add_resource(WeatherID, '/weather')

class WeatherList(Resource):
    def get(self):
        try:
            weather_list = get_weather_info_list()

        except Exception as e:
            return {'error': str(e)}
        else:
            return weather_list

api.add_resource(WeatherList, '/weatherlist')