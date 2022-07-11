# report.py
#
# Exercise 2.4

def read_portfolio(filename):
  '''Computes the total cost (shares*price) of a portfolio file'''
  portfolio = [] 
  error_count = 0 

  with open(filename, 'rt') as f: 
    rows = csv.reader(f)
    # headers = next(rows)
    for row in rows:
      try:
        holding = (row[0], int(row[1]), float(row[2]))
        portfolio.append(holding)
      except ValueError:
        error_count += 1  
        
  return portfolio

file = 'Data/portfolio.csv'

read_portfolio(file)

for r in portfolio:
  print r
