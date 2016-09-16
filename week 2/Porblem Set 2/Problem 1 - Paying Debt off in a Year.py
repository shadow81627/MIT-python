# -*- coding: utf-8 -*-
"""
Calculates the credit card balance after one year if a person only pays the 
minimum monthly payment required by the credit card company each month.

Created on Wed Sep 14 23:23:59 2016

@author: Damien Robinson
"""
#The outstanding balance on the credit card
balance = 484

#Annual interest rate as a decimal
annualInterestRate = 0.2

#Minimum monthly payment rate as a decimal
monthlyPaymentRate = 0.04

#Duration of the repayment period in years
duration = 1

for i in range(0, duration * 12):
    #Calculate the Monthly interest rate
    monthlyInterestRate = annualInterestRate / 12.0
    
    #minimum monthly payment is calculated as monthly payment rate  based on balance
    payment = monthlyPaymentRate * balance
    
    #monthly Unpaied Balance is prvious balance  - monthly payment
    unpaidBalance = balance - payment
    
    #New monthly balance with interest
    balance = unpaidBalance + (monthlyInterestRate * unpaidBalance)
    
#print the remianing balance
print("Remaining balance: " + str(round(balance, 2)))