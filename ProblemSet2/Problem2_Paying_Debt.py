# EDX
# MITx: 6.00.1x Introduction to Computer Science and Programming Using Python
# Problem Set 2
# Problem 2: PAYING DEBT OFF IN A YEAR

def calc_balance(balance, annualInterestRate, fixed_payment):

    for month in range(1,13):
        unpaid_balance = balance - fixed_payment
        balance = unpaid_balance + (annualInterestRate/12*unpaid_balance)

    return balance


def calc_payment(balance, annualInterestRate):

    payment = 10

    for payment in range(10, balance, 10):

        balance_check = calc_balance(balance, annualInterestRate, payment)
        if balance_check < 0:
            break

    return payment

print calc_payment(balance, annualInterestRate)