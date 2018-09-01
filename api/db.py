import firebase_admin
from firebase_admin import credentials, auth, db
import json
import os

def get_weather_info_list():
    weather_list = db.reference('weather_info').get()
    weather_json = {}
    weather_json['data'] = weather_list
    return json.dumps(weather_json)
