# Assignment 6 - Reach Question
# Uses US flight data for 2013, features are airline names, airport codes, departure/arrival times/delays and others.


try:
    import pandas as pd
    import matplotlib.pyplot as plt
    import numpy as np
    import os
except ImportError:
    print('\nPackages pandas, seaborn or matplotlib.pyplot were not imported successfully.\n\n')


def loadfile(filepath):
    return pd.read_csv(filepath)


def cleandata(dframe):
    dframe.drop(dframe.columns[0], inplace=True, axis=1)
    dframe.drop(['alt', 'dst'], inplace=True, axis=1)
    dframe.dropna(how='any', inplace=True)
    return f'\nNull values:\n\n{dframe.isnull().sum()}'


def getcolumnnames(dframe):
    return list(dframe.columns)


def convert_data_types(dframe, col_labels):
    for label in col_labels:
        if label in ('dep_time', 'dep_delay', 'arr_time', 'arr_delay', 'air_time'):
            dframe[label] = dframe[label].astype(dtype='int64')
    return dframe.dtypes


def dataframe_byairline(dframe):
    """For no reason, accepts flight data as a dataframe and returns a dict of dataframes by airline"""
    flightdata_byairline = {}
    for airline in pd.unique(dframe['airlines']):
        flightdata_byairline.update({airline: flightdata[flightdata.airline == airline]})
    return flightdata_byairline



filepath = 'flightdata.csv'

try:
    flightdata = loadfile(filepath)
except IOError:
    print('\n\nFile read error.\n')
    filepath = str(input(r"Please enter a file path (/folder/filename.extension): "))
    flightdata = loadfile(filepath)

# Clean data, verify data types
print(cleandata(flightdata));
flightdata.dtypes

# Get column labels
columnlabels = getcolumnnames(flightdata);

# Convert appropriate time columns to int64 and print data types
convert_data_types(flightdata, columnlabels)

#print(flightdata.corr().to_string())


# Set conditions for line plot
a = flightdata['airline']=='American Airlines Inc.'
b = flightdata['month']==12
c = flightdata['day']==24
d = flightdata['dep_time']
e = flightdata['sched_dep_time']


flightdata[a&b&c&d&e].plot(kind='line', x='sched_dep_time', y= 'dep_time', legend=None)
plt.title('American Airlines: Scheduled vs Actual Departure times (Dec. 24)')
plt.xlabel('Scheduled Times')
plt.ylabel('Actual Times')
os.makedirs('plots/', exist_ok=True)
plt.savefig('plots/AA_24-12_Departures_Sched_vs_Actual__plot.png', dpi=300)
plt.show()
plt.close()

# Set conditions for histogram plot
a = flightdata['airline']=='American Airlines Inc.'
b = flightdata['avgdelay']

flightdata[a&b].hist(column=['avgdelay'], density=1, bins=15, grid=False)
plt.title('American Airlines: Average Flight Delay in 2013')
plt.xlabel('Average Delay (mins)')
plt.ylabel('Distribution')
os.makedirs('plots/', exist_ok=True)
plt.savefig('plots/AA_2013_AvgDelay__hist.png', dpi=300)
plt.show()
plt.close()

# Set conditions for scatter plot
a = flightdata['airline']=='Delta Air Lines Inc.'
b = flightdata['origin'] =='JFK'
c = flightdata['dest']=='LAX'
d = flightdata['dep_delay']
e = flightdata['arr_delay']

flightdata[a&b&c&d&e].plot.scatter(x = 'dep_delay', y='arr_delay')
plt.title('Delta Airlines: JFK to LAX, Departure Delay vs Arrival Delay in 2013')
plt.xlabel('Departure Delay (mins)')
plt.ylabel('Arrival Delay (mins)')
os.makedirs('plots/', exist_ok=True)
plt.savefig('plots/DA-2013-JFK_to_LAX-dep_delay-vs-arr_delay_scatter.png', dpi=300)
plt.show()
plt.close()










