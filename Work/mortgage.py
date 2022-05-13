# mortgage.py
#
# Exercise 1.7-1.11

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
months = 0 

extra_payment_start_month = float(input('Enter extra payment start month:'))
extra_payment_end_month = float(input('Enter extra payment end month:'))
extra_payment = float(input('Enter extra payment amount:'))

while principal > 0:
    months = months+1
    principal = principal * (1+rate/12) - payment
    total_paid = total_paid + payment
    
    if months >= extra_payment_start_month and months <= extra_payment_end_month:
        principal = principal - extra_payment
        total_paid = total_paid + extra_payment
        
    print('Month:',months,'|', 'Total paid:',round(total_paid,2),'|','Remaining principal:',round(principal,2))

print('Total paid:', round(total_paid,2),'over',months-1,'months')
