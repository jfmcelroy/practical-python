# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
months = 0 #or should this be 1?

while principal > 0 and months < 12: #watch out for edge cases
    principal = principal * (1+rate/12) - (payment+1000)
    total_paid = total_paid + (payment+1000)
    months = months+1
    # print('Month:',months,'|', 'Total paid:',round(total_paid,2)) # debugging
    
# print('___________________________WHILE SWITCH___________________________') # debugging
    
while principal > 0 and months >= 12: #do I need to specify anything about months? / do while statements overlap?
    principal = principal * (1+rate/12) - payment
    total_paid = total_paid + payment
    months = months+1
    # print('Month:',months,'|', 'Total paid:',round(total_paid,2)) # debugging
    
print('Total paid:', round(total_paid,2),'over',months,'months')
