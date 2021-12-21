from numpy.core.numeric import NaN
from getdata import getdata
import getdata
import numpy as np
import pandas as pd
import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


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
    distance_xy.append(round(distance_xyi,3))
    i = i + 1

df1 = pd.DataFrame(np.array(latitude_data))

df2 = pd.DataFrame(np.array(longitude_data))
    
df3 = pd.DataFrame(np.array(sample_time_converted))

df4 = pd.DataFrame(np.array(distance_x))

df5 = pd.DataFrame(np.array(distance_y))

df6 = pd.DataFrame(np.array(distance_xy))

df = pd.concat([df1, df2, df3, df4, df5, df6], ignore_index=True, axis=1)
df.columns = ['Latitude', 'Longitude', 'Sample time',
 'Distance in axis x [km]', 'Distance in axis y [km]', 'Distance [km]']

x_values_d3 = [float(x) for x in df['Latitude']]
y_values_d3 = [float(y) for y in df['Longitude']]
z_values_d3 = np.array([t for t, _ in enumerate(df['Sample time'])])

fig1 = plt.figure()
ax = fig1.add_subplot(111, projection='3d')
fig1.set_size_inches(12, 8, forward=True)
ax.plot3D(x_values_d3, y_values_d3, z_values_d3,'g')
ax.scatter(x_values_d3, y_values_d3, z_values_d3)
plt.xlabel('Latitude')
plt.ylabel('Longitude')
plt.show()

fig2 = plt.figure()
fig2.set_size_inches(9, 7)
plt.plot(x_values_d3, y_values_d3)
plt.xlabel('Latitude')
plt.ylabel('Longitude')
plt.grid()
plt.show()

fig3 = plt.figure()
fig3.set_size_inches(9, 7)
plt.plot(z_values_d3, x_values_d3)
plt.xlabel('Time [s]')
plt.ylabel('Latitude')
plt.grid()
plt.show()

fig4 = plt.figure()
fig4.set_size_inches(9, 7)
plt.plot(z_values_d3, y_values_d3)
plt.xlabel('Time [s]')
plt.ylabel('Longitude')
plt.grid()
plt.show()