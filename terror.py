import csv

from datetime import datetime
from matplotlib import pyplot as plt

#Saving the csv file as filename.
filename = 'europe_terrorist_data.csv'

turning the filenam over to an object. 
with open(filename) as f:
  reader = csv.reader(f)
  header_row = next(reader)
  #print(header_row)

  #building arrays to contain the data. 
  dates, countries, countries2, countries3 = [], [], [], []
  #A for loop that will cycle through the CSV file pullign the specific rows of data. 
  for row in reader:
    year = datetime.strptime(row[0], "%Y")
    dates.append(year)

    country = int(row[3])
    countries.append(country)

    country2 = int(row[4])
    countries2.append(country2)

    country3 = int(row[12])
    countries3.append(country3)

#Using matplotlib to graphically represent the data. 
fig = plt.figure(dpi=128, figsize=(10,6))

plt.plot(dates, countries, c="blue")
plt.plot(dates, countries2, c="red")
plt.plot(dates, countries3, c="orange")
plt.title("Terrorist Attacks in Europe, 1970 to Present", fontsize=24)
plt.xlabel("year", fontsize=16)

fig.autofmt_xdate()

plt.ylabel("Number of attacks", fontsize=16)
#The .show() function is what will execute and pull the data to graphically represent it. 
plt.show()


