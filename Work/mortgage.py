# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
months = 1 
extra_payment_start_month = float(input('Enter extra payment start month:'))
extra_payment_end_month = float(input('Enter extra payment end month:'))
extra_payment = float(input('Enter extra payment amount:'))

while principal > 0 and months < extra_payment_start_month: #watch out for edge cases
    principal = principal * (1+rate/12) - payment
    total_paid = total_paid + payment
    print('Month:',months,'|', 'Total paid:',round(total_paid,2)) # debugging
    months = months+1
    
print('___________________________WHILE SWITCH___________________________') # debugging

while principal > 0 and months >= extra_payment_start_month and months <= extra_payment_end_month: #watch out for edge cases
    principal = principal * (1+rate/12) - (payment+extra_payment)
    total_paid = total_paid + (payment+extra_payment)
    print('Month:',months,'|', 'Total paid:',round(total_paid,2)) # debugging
    months = months+1
    
print('___________________________WHILE SWITCH___________________________') # debugging
    
while principal > 0 and months > extra_payment_end_month: #watch out for edge cases
    principal = principal * (1+rate/12) - payment
    total_paid = total_paid + payment
    print('Month:',months,'|', 'Total paid:',round(total_paid,2)) # debugging
    months = months+1
    
print('Total paid:', round(total_paid,2),'over',months-1,'months')
