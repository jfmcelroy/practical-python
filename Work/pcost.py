# pcost.py
#
# Exercise 1.27

total_cost = 0.00

with open('Data/portfolio.csv', 'rt') as f: 
  for line in f:
    cost = float(line.split(',')[2])
    total_cost = total_cost + cost
    
print("Total cost: ", total_cost)
