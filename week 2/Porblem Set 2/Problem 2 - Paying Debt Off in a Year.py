# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 18:40:02 2016

@author: Damien Robinson
"""

#balance - the outstanding balance on the credit card
balance =  36
	     
#annualInterestRate - annual interest rate as a decimal
annualInterestRate = 0.2

#payment to be made each month
payment = 0

#monthly balance with interest
updatedBalanceEachMonth = balance

#while there is still a balance keep trying higher repayments
while updatedBalanceEachMonth > 0:
    #reset updatedBalanceEachMonth 
    updatedBalanceEachMonth = balance
    #increment payment by 10
    payment += 10
    
    #make repayments for 12 months
    for i in range(0, 12):
        #Calculate the Monthly interest rate
        monthlyInterestRate = annualInterestRate / 12.0
        #monthly Unpaied Balance is prvious balance  - monthly payment
        unpaidBalance = updatedBalanceEachMonth - payment
        #New monthly balance with interest
        updatedBalanceEachMonth = unpaidBalance + monthlyInterestRate * unpaidBalance
            
print("Lowest Payment: " + str(payment))