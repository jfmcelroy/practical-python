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
    if months >= extra_payment_start_month and months <= extra_payment_end_month: 
        if payment+extra_payment <= principal:
            principal = principal * (1+rate/12) - (payment+extra_payment)
            total_paid = total_paid + (payment+extra_payment)
        else: 
            total_paid = total_paid + principal
            principal = 0
    
    else: 
        if payment <= principal:
            principal = principal * (1+rate/12) - payment
            total_paid = total_paid + payment
        else:
            total_paid = total_paid + principal
            principal = 0
    
    print(f' {months:4} | ${total_paid:>10.2f} | ${principal:>10.2f}') #monthly table
    # print('Month:',months,'|', 'Total paid:',round(total_paid,2),'|','Remaining principal:',round(principal,2)) #old monthly table output

print(f'Total paid: ${total_paid:0.2f} over {months} months') # final outcome... should it print months-1? Does it depend on the last month case?
