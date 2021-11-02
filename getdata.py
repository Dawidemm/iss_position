from datetime import datetime
import datetime
import requests
import json
import time
from changetf import change_time_format



def getdata(duration):

    longitude_data = []
    latitude_data = []
    sample_time_data = []
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
            sample_time = datetime.datetime.now()
            sample_time_data.append(sample_time)

        else:
            print('Problem with status code')

        i = i + 1

    return longitude_data, latitude_data, sample_time_data

#the method of collecting the sample time data has been changed because,
#by downloading this data from api, we lose information about microseconds at the time of measurement,
#currently we get a sufficiently accurate measurement time for further work