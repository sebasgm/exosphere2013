#!/usr/bin/python

# Importing of an external module to add functionality
import csv

# Reading values from file (Not ready)
#with open('providers.csv','rb') as csv_data:



# We generate three different empty lists for arraging prices
highest_prices = []
medium_prices = []
lowest_prices = []

# Here we are iterating directly over the elements of the dictionary
for price in prices:
    if prices[price] >= 410:
        highest_prices.append(prices[price])
    elif prices[price] < 200:
        lowest_prices.append(prices[price])
    else:
        medium_prices.append(prices[price])

print "Higher prices: ",  highest_prices
print "Medium prices: ", medium_prices
print "Lowest prices: ", lowest_prices



