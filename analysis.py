from numpy.core.numeric import NaN
from getdata import getdata
import getdata
import numpy as np
import pandas as pd
import math
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


duration = int(input('Enter how many seconds the program should download data: '))
downloaded_data = getdata.getdata(duration)

longitude_data = downloaded_data[0]
latitude_data = downloaded_data[1]
sample_time = downloaded_data[2]
    
sample_time_converted = []
for i in range(duration):
    stc = sample_time[i].strftime('%H:%M:%S:%f')
    sample_time_converted.append(stc)

distance_x = [NaN]
i = 0
while i+1 < duration:
    distance_xi = float(latitude_data[i]) - float(latitude_data[i+1])
    if distance_xi < 0:
        distance_xi = distance_xi*(-1)
    distance_x.append(round(distance_xi*1.852, 4))
    i = i + 1

distance_y = [NaN]
i = 0
while i+1 < duration:
    distance_yi = float(longitude_data[i]) - float(longitude_data[i+1])
    if distance_yi < 0:
            distance_yi = distance_yi*(-1)
    distance_y.append(round(distance_yi*1.852, 4))
    i = i + 1

distance_xy = [NaN]
i = 1
while i < duration:
    distance_xyi = math.sqrt(distance_x[i]**2 + distance_y[i]**2)
    distance_xy.append(distance_xyi)
    i = i + 1

longitude_data_array = np.array(longitude_data)
df1 = pd.DataFrame(longitude_data_array)

latitude_data_array = np.array(latitude_data)
df2 = pd.DataFrame(latitude_data_array)
    
sample_time_array = np.array(sample_time_converted)
df3 = pd.DataFrame(sample_time_array)

distance_x_array = np.array(distance_x)
df4 = pd.DataFrame(distance_x_array)

distance_y_array = np.array(distance_y)
df5 = pd.DataFrame(distance_y_array)

distance_xy_array = np.array(distance_xy)
df6 = pd.DataFrame(distance_xy_array)

df = pd.concat([df1, df2, df3, df4, df5, df6], ignore_index=True, axis=1)
df.columns = ['longitude', 'latitude', 'sample time', 'distance in axis x [km]', 'distance in axis y [km]', 'distance [km]']
print(df)