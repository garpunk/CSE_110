'''
Name: Garrett Helms
Date: May 27th 2024
File: loan.py

purpose- calculate if person is eligible for loan based off self-reported rating


'''

loan_size = int(input("How large is the loan? rating from 1–10 "))

credit_history = int(input("How good is your credit history? rating from 1–10 "))
income = int(input("How high is your income? rating from 1–10 "))
down_payment = int(input("How large is your down payment? rating from 1–10 "))

decision = ""

if loan_size >= 5:
    if credit_history >= 7 and income >= 7:
        decision = "yes"
    elif credit_history >= 7 or income >= 7:
        if down_payment >= 5:
            decision = "yes"
        else: 
         decision = "no"
else:
    if credit_history < 4:
        decision = "no"
    elif income >= 7 or down_payment >= 7:
        decision = "yes"
    elif income >= 4 and down_payment >= 4:
        decision = "yes"
    else: decision = "no"

print(f"The final decision is {decision}")