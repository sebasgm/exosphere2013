#!/usr/bin/python

# Generated dictionary of values that could be prices of given products,or any other thing
prices = {'provider_1': 156, 
          'provider_2': 148,
          'provider_3': 245,
          'provider_4': 134,
          'provider_5': 415,
          'provider_6': 345,
          'provider_7': 768,
          'provider_8': 654,
          'provider_9': 341,
          'provider_10': 346,
          'provider_11': 367,
          'provider_12': 378,
          'provider_13': 519,
          'provider_14': 910,
          'provider_15': 815,
         }

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



