import csv
import collections
from datetime import datetime
import matplotlib.font_manager as fm
from matplotlib import pyplot as plt

plt.rcParams['font.family'] = 'Times New Roman'
# Get dates, high, and low temperatures from file.
filename = 'geoMap.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    Countries, Interests = [], []
#try catch for missing data
    for row in reader:
        try:
            Country = (row[0])
            Interest = int(row[1])
        except ValueError:
            print(Country, 'missing data')
        else:
            Countries.append(Country)
            Interests.append(Interest)
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99', '#c196e7', '#4debe7']
plt.pie(Interests, labels=Countries,colors=colors, autopct='%1.1f%%', shadow=False, startangle=90)
centre_circle = plt.Circle((0,0),0.70,fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()
