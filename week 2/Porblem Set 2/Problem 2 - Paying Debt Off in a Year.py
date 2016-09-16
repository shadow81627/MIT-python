# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 18:40:02 2016

@author: Damien Robinson
"""

    balance - the outstanding balance on the credit card

    annualInterestRate - annual interest rate as a decimal

Monthly interest rate = (Annual interest rate) / 12.0
Monthly unpaid balance = (Previous balance) - (Minimum fixed monthly payment)
Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance) 