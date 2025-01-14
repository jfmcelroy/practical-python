# readprices.py

# Exercise 2.6
# housing the read_prices() function

import csv # may not need this
from pprint import pprint # can we just write "import pprint"?

def read_prices(filename):
  '''reads prices into a dictionary with stock names as keys'''
  prices = {}
  error_count = 0 
  with open(filename, 'rt') as f: 
    rows = csv.reader(f)
    # headers = next(rows) # no headers in this file? 
    for row in rows:
      if isinstance(row[0],str) == True: # and ( isinstance(row[1],float) or isinstance(row[1],int)): 
        name = row[0]
        prices[name] = float(row[1]) # or is it prices['name'] ?
      else: # or more ifs?
        error_count += 1
        
  return (prices, error_count)

file = 'Data/prices.csv'

pprint(read_prices(file)[0])

print(f'{read_prices(file)[1]} row(s) with value error')
