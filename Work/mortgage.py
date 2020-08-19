# mortgage.py
#
# Exercise 1.7

principal = 5.0e5
rate = 0.05
payment = 2684.11
total_paid = 0.0
month = 1

extra_payment_start_month = 61
extra_payment_end_month = 108

while principal > 0:
    if (month <= extra_payment_end_month) and (month >= extra_payment_start_month):
        extra_payment = 1000
    else:
        extra_payment = 0

    if principal >= payment + extra_payment:
        principal = principal * (1 + rate/12) - payment - extra_payment
    else:
        payment = principal
        extra_payment = 0.0
        principal = 0.0
    total_paid = total_paid + payment + extra_payment

    print(month, round(total_paid, 2), round(principal, 2))

    month += 1


print('Months', month-1)
print('Total paid', round(total_paid, 5))
