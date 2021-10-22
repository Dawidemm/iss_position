import requests
import json
import time
from datetime import datetime


def getdata(duration):

    longitude_data = []
    latitude_data = []
    i = 0

    while i < int(duration):
        time.sleep(1)
        url = 'http://api.open-notify.org/iss-now.json'
        answer = requests.get(url)

        if answer.status_code == 200:
            answer = json.loads(answer.text)
            position = answer['iss_position']
            longitude = position['longitude']
            latitude = position['latitude']
            latitude_data.append(latitude)
            longitude_data.append(longitude)
            #print(latitude, longitude)

        else:
            print('Problem with status code')

        i = i + 1

    return longitude_data, latitude_data
