# pcost.py
#
# Exercise 1.27

total_cost = 0.00

with open('Data/portfolio.csv', 'rt') as f: 
  for line in f:
    total_cost = total_cost + line.split(,)[2]
    
