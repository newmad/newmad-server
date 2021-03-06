from flask import Flask
from flask_restful import reqparse, Resource, Api
import os
import requests
from .db import *
from flask_cors import CORS

DB_SERVER = os.environ.get('DB_SERVER', None)
API_KEY = os.environ.get('API_KEY', None)

cred = credentials.Certificate('./namedserviceAccountKey.json')
default_app = firebase_admin.initialize_app(cred, {
    'databaseURL' : DB_SERVER
})


app = Flask(__name__)
CORS(app)
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

class Place(Resource):
    def post(self):
        pass

    def get(self, sorted='like'):
        try:
            place_list = get_place_list(sorted)
        except Exception as e:
            return {'error': str(e)}
        else:
            return place_list    

api.add_resource(Place, '/place', '/place/<string:sorted>')


class Search(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('keyword', type=str)
        args = parser.parse_args()

        _keyword = args['keyword']

        place = search_place(_keyword)

        return place

api.add_resource(Search, '/search', endpoint='search')

class SearchById(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('id', type=int)
        args = parser.parse_args()

        _id = args['id']

        place = search_id(_id)

        return place

api.add_resource(SearchById, '/searchid', endpoint='searchid')

class Like(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('keyword', type=int)
        args = parser.parse_args()

        _keyword = args['keyword']

        place = set_update_like(_keyword)

        return place

api.add_resource(Like, '/like', endpoint='like')

class PlaceByWeather(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('keyword', type=str)
        args = parser.parse_args()

        _keyword = args['keyword']

        place = get_place_list_by_weather(_keyword)

        return place

api.add_resource(PlaceByWeather, '/placebyweather', endpoint='placebyweather')