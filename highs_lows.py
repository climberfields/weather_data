import csv

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

    highs = []
    for row in reader:
        # Take the data and convert it from a string to an integer so it can be read on matplot
        high = int(row[1])
        highs.append(high)


    print(highs)