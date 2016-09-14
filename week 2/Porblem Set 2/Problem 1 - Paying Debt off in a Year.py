# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 23:23:59 2016

@author: Damien Robinson
"""

balance = 42
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

Remaining balance:
    
Monthly interest rate= (Annual interest rate) / 12.0
Minimum monthly payment = (Minimum monthly payment rate) x (Previous balance)
Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance) 