# report.py
#
# Exercise 2.4

import csv
from pprint import pprint #should this go hear or nearer to where we use it?

def read_portfolio(filename):
  '''Computes the total cost (shares*price) of a portfolio file'''
  portfolio = [] #change from tuple to list?
  error_count = 0 

  with open(filename, 'rt') as f: 
    rows = csv.reader(f)
    # headers = next(rows)
    for row in rows:
      try:
        holding = {
          'name': row[0], 
          'shares': int(row[1]), 
          'price': float(row[2])
        }
        portfolio.append(holding) 
      except ValueError:
        error_count += 1  
        
  return (portfolio, error_count)

file = 'Data/portfolio.csv'
total = 0.00

#for r in read_portfolio(file)[0]:
#  print(r)
#print(read_portfolio(file)[0]) 
pprint(read_portfolio(file)[0]) 

for r in read_portfolio(file)[0]:
  total += r['shares']*r['price']
  
print(f'Total cost: ${total}')

print(f'{read_portfolio(file)[1]} row(s) with value error')
