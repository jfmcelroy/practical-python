# pcost.py
#
# Exercise 1.27, 1.32

import csv

def portfolio_cost(filename):
  total_cost = 0.00 
  error_count = 0 

  with open(filename, 'rt') as f: 
    rows = csv.reader(f)
    next(rows)
    for row in rows:
      try:
        cost = float(row[2]) #already float?
        total_cost += cost
      except ValueError:
        error_count += 1  
        
  return [total_cost, error_count]
    
file = 'Data/portfolio.csv' #change for user input
    
print(f'Total cost: ${portfolio_cost(file)[0]:0.2f}')

print(f'{portfolio_cost(file)[1]} row(s) with value error')
