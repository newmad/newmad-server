import firebase_admin
from firebase_admin import credentials, auth, db
import json
import os

def get_weather_info_list():
    weather_list = db.reference('weather_info').get()
    weather_json = {}
    weather_json['data'] = weather_list
    return json.dumps(weather_json)

# sorted : like / blahblah
def get_place_list(sorted='like'):
    ref = db.reference('place_info')
    place_list = dict()
    for key,value in reversed(list(ref.order_by_child(sorted).get().items())):
        place_list[key] = value
    return json.dumps(place_list)

    
def set_place():
    pass