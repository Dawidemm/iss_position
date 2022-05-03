from numpy.core.numeric import NaN
from getdata import getdata
import getdata
import numpy as np
import pandas as pd
import math
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from linreg_model import LinearRegression


def charts_2d(x, y, xlabel, ylabel):
    fig = plt.figure()
    fig.set_size_inches(9, 7)
    plt.plot(x, y)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(color='black', linestyle='--')
    plt.show()
    return None

def linreg_plot(X, y, model):
    fig = plt.figure()
    fig.set_size_inches(9, 7)
    plt.scatter(X, y, c='steelblue', s=50)
    plt.plot(X, model.predict(X), color='red', lw=1)
    plt.grid(color='black', linestyle='--')
    plt.show()
    return None

def count_distance(duration, latitude_distance, longitude_distance):
    dist_x = [NaN]
    dist_y = [NaN]
    dist_xy = [NaN]

    for i in range(duration-1):
        c_dist_x = float(latitude_distance[i]) - float(latitude_distance[i+1])
        c_dist_y = float(longitude_distance[i]) - float(longitude_distance[i+1])

        if c_dist_x < 0:
            c_dist_x = c_dist_x * (-1)
        dist_x.append(round(c_dist_x * 120.324, 3))

        if c_dist_y < 0:
            c_dist_y = c_dist_y * (-1)
        dist_y.append(round(c_dist_y * 120.324, 3))

    for i in range(1,duration):
        c_dist_xy = math.sqrt(dist_x[i]**2 + dist_y[i]**2)
        dist_xy.append(round(c_dist_xy, 3))

    return dist_x, dist_y, dist_xy

def main():

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

    df1 = pd.DataFrame(np.array(latitude_data))

    df2 = pd.DataFrame(np.array(longitude_data))
        
    df3 = pd.DataFrame(np.array(sample_time_converted))

    df4 = pd.DataFrame(np.array(count_distance(duration,latitude_data,longitude_data)[0]))

    df5 = pd.DataFrame(np.array(count_distance(duration,latitude_data,longitude_data)[1]))

    df6 = pd.DataFrame(np.array(count_distance(duration,latitude_data,longitude_data)[2]))

    df = pd.concat([df1, df2, df3, df4, df5, df6], ignore_index=True, axis=1)
    df.columns = ['Latitude', 'Longitude', 'Sample time',
    'Distance in axis x [km]', 'Distance in axis y [km]', 'Distance [km]']
    latitude_values = [float(x) for x in df['Latitude']]
    longitude_values = [float(y) for y in df['Longitude']]
    time_seconds = np.array([t for t, _ in enumerate(df['Sample time'])])
    
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    fig.set_size_inches(12, 8, forward=True)
    ax.plot3D(latitude_values, longitude_values, time_seconds,'g')
    ax.scatter(latitude_values, longitude_values, time_seconds)
    plt.xlabel('Latitude')
    plt.ylabel('Longitude')
    plt.show()

    charts_2d(latitude_values, longitude_values, 'Latitude', 'Longitude')
    charts_2d(time_seconds, latitude_values, 'Time [s]', 'Latitude')
    charts_2d(time_seconds, longitude_values, 'Time [s]', 'Longitude')

    X = df[['Latitude']].values
    y = df[['Longitude']].values
    sc_x = StandardScaler()
    sc_y = StandardScaler()
    X_std = sc_x.fit_transform(X)
    y_std = sc_y.fit_transform(y[: np.newaxis]).flatten()

    lr = LinearRegression(0.01, 30)
    lr.fit(X_std, y_std)
    linreg_plot(X_std, y_std, lr)

main()