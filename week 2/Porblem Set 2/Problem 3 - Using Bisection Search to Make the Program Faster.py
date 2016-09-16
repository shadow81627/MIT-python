# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 20:44:18 2016

@author: Damien Robinson
"""

#balance - the outstanding balance on the credit card
balance =  999999
	     
#annualInterestRate - annual interest rate as a decimal
annualInterestRate = 0.18

#Calculate the Monthly interest rate
monthlyInterestRate = annualInterestRate / 12.0

#monthly balance with interest
updatedBalanceEachMonth = balance

#Monthly payment lower boundary for bisectional search
lower = balance / 12
#Monthly payment upper bounary for bisectional search
upper = (balance * (1 + monthlyInterestRate) ** 12) / 12.0 

#while there is still a balance keep trying higher repayments
while round(updatedBalanceEachMonth, 2) != 0:
    #middle point between upper payment and lower payment
    payment = (lower + upper) / 2
    #reset updatedBalanceEachMonth 
    updatedBalanceEachMonth = balance
    
    #make repayments for 12 months
    for i in range(0, 12):
        #monthly Unpaied Balance is prvious balance  - monthly payment
        unpaidBalance = updatedBalanceEachMonth - payment
        #New monthly balance with interest
        updatedBalanceEachMonth = unpaidBalance + monthlyInterestRate * unpaidBalance
        
    if updatedBalanceEachMonth > 0:
        #if the the updated balance is greater than 0 then the payment was too small
        lower = payment
    elif updatedBalanceEachMonth < 0:
        #if the the updated balance is smaller than 0 then the payment was too large
        upper = payment
print("Lowest Payment: " + str(round(payment, 2)))