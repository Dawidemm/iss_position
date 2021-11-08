from numpy.core.fromnumeric import size
from numpy.core.numeric import NaN
from getdata import getdata
import getdata
import numpy as np
import pandas as pd
import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation


duration = int(input('Enter how many seconds the program should download data: '))
print('\n')
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
    distance_x.append(round(distance_xi*120.324, 3))
    i = i + 1

distance_y = [NaN]
i = 0
while i+1 < duration:
    distance_yi = float(longitude_data[i]) - float(longitude_data[i+1])
    if distance_yi < 0:
            distance_yi = distance_yi*(-1)
    distance_y.append(round(distance_yi*120.324, 3))
    i = i + 1

distance_xy = [NaN]
i = 1
while i < duration:
    distance_xyi = math.sqrt(distance_x[i]**2 + distance_y[i]**2)
    distance_xy.append(distance_xyi)
    i = i + 1

latitude_data_array = np.array(latitude_data)
df1 = pd.DataFrame(latitude_data_array)

longitude_data_array = np.array(longitude_data)
df2 = pd.DataFrame(longitude_data_array)
    
sample_time_array = np.array(sample_time_converted)
df3 = pd.DataFrame(sample_time_array)

distance_x_array = np.array(distance_x)
df4 = pd.DataFrame(distance_x_array)

distance_y_array = np.array(distance_y)
df5 = pd.DataFrame(distance_y_array)

distance_xy_array = np.array(distance_xy)
df6 = pd.DataFrame(distance_xy_array)

df = pd.concat([df1, df2, df3, df4, df5, df6], ignore_index=True, axis=1)
df.columns = ['Latitude', 'Longitude', 'Sample time',
 'Distance in axis x [km]', 'Distance in axis y [km]', 'Distance [km]']
print(df)

x_values_d3 = [float(x) for x in df['Latitude']]
y_values_d3 = [float(y) for y in df['Longitude']]
z_values_d3 = np.array([t for t, _ in enumerate(df['Sample time'])])

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
fig.set_size_inches(12, 9, forward=True)
ax.plot3D(x_values_d3, y_values_d3, z_values_d3,'g')
ax.scatter(x_values_d3, y_values_d3, z_values_d3)
plt.xlabel('Latitude')
plt.ylabel('Longitude')
plt.show()

plt.plot(x_values_d3, y_values_d3)
plt.show()