# pcost.py
#
# Exercise 1.27, 1.32

import csv

def portfolio_cost(filename):
  total_cost = 0.00

  with open(filename, 'rt') as f: #syntax for 'filename'
    rows = csv.reader(f)
    next(rows)
    for row in rows: 
      cost = float(row[2]) #already float?
      total_cost = total_cost + cost

  return round(total_cost,2)
    
file = 'Data/portfolio.csv' #change for user input

portfolio_cost(file)
    
print(f'Total cost: ${total_cost:0.2f}')
