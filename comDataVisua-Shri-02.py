"""
Program: Commodity Data Visualization
Author: Shrikant Sharma
Description: Filtering the Data and Plotting a line Graph
Filename: comDataVisua-shri-02.py
Purpose: data filtering and plotting a line graph
Revisions:
    00: Import all the packages
    01: Announcement of the program
    02: Convert the date and prices 
    03: Select the data of Oranges in Chicago
    04: Plot the graph for oranges in Chicago
"""
# there are no literal constants
# there are no class definitions
# there are no function definitions
# title of the program
import matplotlib.ticker as mtick
import matplotlib.pyplot as plt
from datetime import datetime
import csv
#STEP 1
# Import all the required packages

with open("produce_csv.csv", 'r') as csvfile:
    reader = csv.reader(csvfile)
    data = [row for row in reader]
#STEP 2 (Announce)
# title of the program
print('Program to filter the data and plotting line graph')

#STEP 3
# Convert the date and prices
# Initialise new list to receive data
modData = []
for row in data:
    # empty row to receive values
    newrow = list()
    # transverse the values in the old rows
    for item in row:
        # test for price string and convert
        if "$" in item:
            newrow.append(float(item.replace("$", "")))
        # test for the date and convert
        elif "/" in item:
            newrow.append(datetime.strptime(item, "%m/%d/%Y"))
         # if not date or price apped to the newrow
        else:
            newrow.append(item)
    modData.append(newrow)


# Creating the new data records
# remove the header
locations = modData.pop(0)[2:]
# initialise new list for data records
records = list()
# trasverse each row
for row in modData:
    # first two values are common for all tthe locations
    newrow = row[:2]
    # transverse the locations and prices
    for loc, price in zip(locations, row[2:]):
        # add a new data record
        records.append(newrow+[loc, price])

#STEP 4
# Select the data of Oranges in Chicago

# filter the data
select = list(
    filter(lambda x: x[0] == "Oranges" and x[2] == "Chicago", records))

# dates and prices for plot
dates = [x[1] for x in select]
prices = [x[3] for x in select]

dpmerge = [[d, p] for d, p in zip(dates, prices)]
dpmerge.sort(key=lambda a: a[0])

for x in dpmerge:
    print(f'{datetime.strftime(x[0],"%m-%d-%Y")} {int(25*x[1])*"="}')

#STEP 5
# Plot the graph for oranges in Chicago
# create a figure
fig = plt.figure()
# add an axis to the figure
ax = fig.add_subplot()

# add the data series
ax.plot(dates, prices, label="Oranges in Chicago")
# title for the x-axis
ax.set_xlabel('date')
# title for the y-axis
ax.set_ylabel('price in dollars')
ax.set_title('The Cost of Oranges in Chicago\n from 03/2017 to 03/2018')
# format for dollars and cents
fmt = '${x:,.2f}'
# define the format
tick = mtick.StrMethodFormatter(fmt)
# establish the table for y-axis
ax.yaxis.set_major_formatter(tick)
# add legend
plt.legend()
# show the figures
plt.show()
