# pcost.py
#
# Exercise 1.27

total_cost = 0.00

with open('Data/portfolio.csv', 'rt') as f: 
  next(f)
  for line in f:
    cost = float(line.split(',')[2][:-1])
    total_cost = total_cost + cost
    
round(total_cost,2)
    
print(f'Total cost: ${total_paid:0.2f}')
