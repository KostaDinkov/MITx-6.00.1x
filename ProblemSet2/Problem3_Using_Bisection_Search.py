# EDX
# MITx: 6.00.1x Introduction to Computer Science and Programming Using Python
# Problem Set 2
# Problem 3: USING BISECTION SEARCH TO MAKE THE PROGRAM FASTER


def calc_year_balance(balance, annualInterestRate, fixed_payment):

    r = annualInterestRate/12
    for month in range(12):
        updated_balance = balance - fixed_payment
        balance = updated_balance +r* updated_balance

    return balance


def calc_payment(balance, annualInterestRate):

    r = annualInterestRate / 12
    eps = 0.01
    low = balance / 12.0
    high = (balance * (1 + r)**12)/12.0
    pay = (low+high) / 2
    balance_check = calc_year_balance(balance, annualInterestRate, pay)

    while abs(balance_check) > eps:

        balance_check = calc_year_balance(balance, annualInterestRate, pay)

        if balance_check > 0:
            low = pay
            pay = (low+high) / 2

        elif balance_check < 0:
            high = pay
            pay = (low + high)/2

    return round(pay, 2)

print calc_payment(balance, annualInterestRate)




