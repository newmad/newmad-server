from flask import Flask
from flask_restful import Resource, Api
import os
import requests

API_KEY = os.environ.get('API_KEY', None)

app = Flask(__name__)
api = Api(app)

class WeatherID(Resource):
    def get(self):
        try:
            url = 'https://api.openweathermap.org/data/2.5/weather?q=Jeju,KR&appid=' + API_KEY
            response = requests.get(url)
            return response.text

        except Exception as e:
            return {'error': str(e)}

api.add_resource(WeatherID, '/weather')

'''
class WeatherGEO(Resource):
    def post(self):
        try:
            pass
        except Exception as e:
            return {'error': str(e)}
'''