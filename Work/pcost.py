# pcost.py
#
# Exercise 1.27, 1.32

import csv

total_cost = 0.00

with open('Data/portfolio.csv', 'rt') as f: 
  rows = csv.reader(f)
  next(rows)
  for row in rows: 
    cost = float(row[2]) #already float?
    total_cost = total_cost + cost
    
round(total_cost,2)
    
print(f'Total cost: ${total_cost:0.2f}')
