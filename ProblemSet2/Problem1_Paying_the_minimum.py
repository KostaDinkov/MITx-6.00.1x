# EDX
# MITx: 6.00.1x Introduction to Computer Science and Programming Using Python
# Problem Set 2
# Problem 1: Paying the minimum

def calc_new_balance(old_balance, annual_ir, minimum_mp):

    monthly_ir = annual_ir/12
    monthly_ub = old_balance - minimum_mp

    return monthly_ub +(monthly_ir * monthly_ub)


def calc_min_month_payment(old_balance, min_monthly_pr):

    return old_balance * min_monthly_pr


def calc_year_balance (balance, annualInterestRate, monthlyPaymentRate):

    total_paid = 0
    for month in range(1, 13):
        print ("Month: " + str(month))

        min_monthly_payment = round(calc_min_month_payment(balance, monthlyPaymentRate), 2)
        total_paid += min_monthly_payment
        print ("Minimum monthly payment: " + str(min_monthly_payment))

        balance = round(calc_new_balance(balance, annualInterestRate, min_monthly_payment), 2)
        print ("Remaining balance: " + str(balance))

    print("Total paid: " + str(total_paid))
    print("Remainging balance: " + str(balance))



#balance = 4213
#annualInterestRate = 0.2
#monthlyPaymentRate = 0.04

calc_year_balance(balance, annualInterestRate, monthlyPaymentRate)
