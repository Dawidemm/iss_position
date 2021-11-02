from getdata import getdata
from datetime import datetime
import getdata
import numpy as np
import pandas as pd


def main():
    duration = int(input('Enter how many seconds the program should download data: '))
    downloaded_data = getdata.getdata(duration)

    longitude_data = downloaded_data[0]
    latitude_data = downloaded_data[1]
    sample_time = downloaded_data[2]
    
    sample_time_converted = []
    for i in range(duration):
        stc = sample_time[i].strftime('%H:%M:%S:%f')
        sample_time_converted.append(stc)

    longitude_data_array = np.array(longitude_data)
    df1 = pd.DataFrame(longitude_data_array)

    latitude_data_array = np.array(latitude_data)
    df2 = pd.DataFrame(latitude_data_array)
    
    sample_time_array = np.array(sample_time_converted)
    df3 = pd.DataFrame(sample_time_array)

    df = pd.concat([df1, df2, df3], ignore_index=True, axis=1)
    df.columns = ['longitude', 'latitude', 'sample time']
    print(df)
    
main()
