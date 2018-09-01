import firebase_admin
from firebase_admin import credentials, auth, db
import json
import os



def get_weather_info_list():
    DB_SERVER = os.environ.get('DB_SERVER', None)
    cred = credentials.Certificate('./namedserviceAccountKey.json')
    default_app = firebase_admin.initialize_app(cred, {
        'databaseURL' : DB_SERVER
    })
    weather_list = db.reference('weather_info').get()
    weather_json = {}
    weather_json['data'] = weather_list
    return json.dumps(weather_json)
