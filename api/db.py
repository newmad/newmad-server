from firebase_admin import credentials, auth, db
import firebase_admin
import json
import os


def get_weather_info_list():
    weather_list = db.reference('weather_info').get()
    weather_json = {}
    weather_json['data'] = weather_list
    return json.dumps(weather_json, ensure_ascii = False)


# sorted : like / blahblah
def get_place_list(sorted):
    ref = db.reference('place_info')
    place_list = dict()
    for key,value in reversed(list(ref.order_by_child(sorted).get().items())):
        place_list[key] = value
    return json.dumps(place_list, ensure_ascii = False)


def get_place_list_by_weather(keyword):
    ref = db.reference('place_info')
    place = dict(ref.order_by_child('weather-id').equal_to(keyword).get())
    return json.dumps(place, ensure_ascii = False)


def search_place(keyword):
    ref = db.reference('place_info')
    place = dict(ref.order_by_child('title').start_at(keyword).end_at(keyword + u'\uf8ff').get())
    return json.dumps(place, ensure_ascii = False)

def search_id(id):
    ref = db.reference('place_info')
    place = dict(ref.order_by_child('id').equal_to(id).get())
    return json.dumps(place, ensure_ascii = False)

def set_update_like(placeId):
    ref = db.reference('place_info')
    place = ref.order_by_child('id').equal_to(placeId).get()
    targetTitle = list(place)[0]
    likeData = ref.order_by_child('id').equal_to(placeId).get()[targetTitle]['like']
    title = ref.order_by_child('id').equal_to(placeId).get()[targetTitle]['title']
    place[title].update({'like':likeData+1})
    ref.update({title: place[title]})
    return json.dumps(place[title], ensure_ascii = False)