# -*- coding: utf-8 -*-

'''
Program: Analysis of Commodity Data
Author: Shrikant Sharma
Description: Analysis of the Commodity Data by reading, organizing, selecting, consolidating, and generating a graphical representation of data
Filename: finalProject-shri-02.py
Purpose: Analysis of Commodity Data
Revision:
01: Used Zip, enumerate, join, map, plotly, datetime.
02: defined functions for average and printing
03: prompted the user for the inputs and generated graphs for the selected commodities' average price.
'''
# there are no class definitions
# there are no literal constants
# title of the program
from datetime import datetime
import plotly.graph_objs as go
import plotly.offline as py
import csv
print("Program to Analyze commodity data")

print("="*26)
print("Analysis of Commodity Data")
print("="*26)


def columnPrint(x, enum=1, wid=20):

'''
def columnPrint(x, enum=1, wid=20) prints all the items from the data
'''
   s = ''
       for n, item in enumerate(x):
            if len(s) < 3*(wid+enum+2):
                if enum:
                    s += f"<{n:2}>"  # add index in brackets
                s += f" {item:<20}"  # add the item text
            else:
                print(s)  # print 3 columns
                s = ''  # start the next 3 columns

                if enum:
                    s += f'<{n:2}>'  # add index in brackets
                s += f' {item:<20}'  # add the item text
        if s:
            print(s)


def columnDatePrint(x, enum=1, wid=30):

'''
def columnDatePrint(x, enum=1, wid=30) prints dates of all the items from the data
'''
   s = ''
    for n, item in enumerate(x):
        if len(s) < 3*(wid+enum+2):
            if enum:
                s += f"<{n:2}>"  # add index in brackets
            # add the item text
            s += f" {datetime.strftime(item,'%Y-%m-%d'):<15}"
        else:
            print(s)  # print 3 clumns
            s = ''  # start the next 3 columns

            if enum:
                s += f'<{n:2}>'  # add index in brackets
            # add the item text
            s += f" {datetime.strftime(item,'%Y-%m-%d'):<15}"
    if s:
        print(s)


def average(x):

'''
def average(x) returns the average
'''
   if len(x) == 0:
        return 0
    else:
        return sum(x)/len(x)


# reading the data
with open('produce_csv.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    data = [row for row in reader]

# convert the date and time and price to float
modData = []  # new list to receive data
for row in data:
    newRow = list()  # empty row to receive values
    for item in row:
        if '$' in item:  # test for price and convert
            newRow.append(float(item.replace("$", "")))
        elif "/" in item:  # test for date and convert
            newRow.append(datetime.strptime(item, '%m/%d/%Y'))
        else:
            newRow.append(item)
    modData.append(newRow)

# initializing data records
locations = modData.pop(0)[2:]  # remove header and slice
records = list()  # empty list for data records
for row in modData:
    newRow = row[:2]  # first 2 values are common for all locations
    for loc, price in zip(locations, row[2:]):
        records.append(newRow+[loc, price])  # add to records

print("\nSELECT PRODUCT BY NUMBER ...")
commodity_List = list({i[0] for i in records})
commodity_List.sort()
columnPrint(commodity_List)
product = [int(i) for i in input(
    "Enter product numbers separated by spaces: ").split()]
product1 = [commodity_List[i] for i in product]
print(f"selected poducts: {' '.join(map(str,product1))} \n")

print('\nSELECT DATE RANGE BY NUMBER...')
date_list = list({i[1] for i in records})
date_list.sort()
columnDatePrint(date_list)
print(
    f"Earliest available date is : {datetime.strftime(date_list[0],'%Y-%m-%d')}")
print(
    f"Latest available date is : {datetime.strftime(date_list[-1],'%Y-%m-%d')}")
date = [int(i) for i in input(
    "Enter start/end date numbers separated by a space: ").split()]
date1 = [datetime.strftime(date_list[i], '%Y-%m-%d') for i in date]
print(
    f"Dates from  {''.join(map(str,date1[0]))} to {''.join(map(str,date1[1]))}")
start_date = datetime.strptime(date1[0], '%Y-%m-%d')
end_date = datetime.strptime(date1[1], '%Y-%m-%d')

# create a list of locations
print("\nSELECT LOCATIONS BY NUMBER ...")
locations.sort()
for (i, j) in enumerate(locations):
    print(f"<{i}> {j}")
location = [int(i) for i in input(
    f"Enter location numbers separated by spaces: ").split()]
location1 = [locations[i] for i in location]
print(f"Selected locations: {' '.join(map(str,location1))}")

# Create a list for user options
user_option = list(filter(lambda i: i[0] in product1 and (
    start_date <= i[1] <= end_date) and i[2] in location1, records))

print(user_option)
print(f"{len(user_option)} records have been selected.")

# Create dictionary for user options
dict_data = {}
for i in location1:
    dict_data[i] = {}
    for k in product1:
        dict_data[i].update({k: []})
        dict_data[i][k] = [x[3]
                           for x in user_option if x[2] == i and x[0] == k]

# Calculating the average of prices of user selected options
dataPlot = {}
for q in dict_data:
    dataPlot.update({q: {}})
    for p in dict_data[q]:
        dataPlot[q].update({p: average(dict_data[q][p])})

# Traverse dictionary to create list of plotly traces
traceBar = []
for loca in location1:
    price_list = [dataPlot[loca][product] for product in product1]
    traceBar.append(go.Bar(x=product1, y=price_list, name=loca))
layout = go.Layout(
    barmode='group'
)

# Update the figure layout
fig = go.Figure(data=traceBar, layout=layout)
fig.update_layout(
    title=f"Product prices from {date1[0]} through {date1[1]}",
    xaxis_title="Product",
    yaxis_title="Average Price"
)

# plot the figure to the html file
fig.update_layout(yaxis_tickformat='$.2f')
py.plot(fig, filename='Produce_Bar_Graph_Analysis.html')
fig.show()
