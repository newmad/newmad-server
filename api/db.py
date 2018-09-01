from firebase_admin import credentials, auth, db
import firebase_admin
import json
import os


def get_weather_info_list():
    weather_list = db.reference('weather_info').get()
    weather_json = {}
    weather_json['data'] = weather_list
    return json.dumps(weather_json)


# sorted : like / blahblah
def get_place_list(sorted):
    ref = db.reference('place_info')
    place_list = dict()
    for key,value in reversed(list(ref.order_by_child(sorted).get().items())):
        place_list[key] = value
    return json.dumps(place_list)


def set_place():
    pass


def search_place(keyword):
    ref = db.reference('place_info')
    place = dict(ref.order_by_child('title').start_at(keyword).end_at(keyword + u'\uf8ff').get())
    return json.dumps(place)