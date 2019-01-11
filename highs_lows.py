import csv
from datetime import datetime

from matplotlib import pyplot as plt



#filename is the name of the file and data we are working with
filename = 'sitka_weather_07-2014.csv'

#with open opens the file (filename) as object f for the naming convention
with open(filename) as f:
# we pass f as the argument for the csv.reader which we downloaded through importing csv
    reader = csv.reader(f)
#we use the next function to show us the next line in the file when passed as the reader object
    header_row = next(reader)
    print(header_row)

    # for index, column_header in enumerate(header_row):
    #     print(index, column_header)

    dates, highs = [], []
    for row in reader:
        current_date = datetime.strptime(row[0], "%Y-%m-%d")
        dates.append(current_date)
        # Take the data and convert it from a string to an integer so it can be read on matplot
        high = int(row[1])
        highs.append(high)


    print(highs)

# plot data

fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c= 'red')
fig.autofmt_xdate()
# Format plot.

plt.title("Daily high temperatures, July 2014", fontsize=24)
plt.xlabel('', fontsize=16)
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()