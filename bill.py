# -*- coding: utf-8 -*-
"""
Created on Wed Sep 03 20:49:36 2014

@author: danie_000
"""

print (' Hi, Welcome to the Awesome Program of Sales for MA , or APSM, made by Daniel.')
cost = float(raw_input ("Insert the value of your bill "))
tax = (1.0625) #Tax + Bill
tip = (0.15) #Just tips
tax_total = float(cost*tax)
tip_total = float(cost*tip)
total = float(tax_total + tip_total) # 
print ("%.2f is your total with tips. " % total) # Just using 2 numbers after the . !
from datetime import datetime #importing the date of your computer
now = datetime.now()

print '%s/%s/%s %s:%s:%s' % (now.month, now.day, now.year, now.hour, now.minute, now.second)

MakeMeTrue = raw_input("What is my age? ") #I am not sure about this.
if MakeMeTrue == 21 :
    print('True')
else :
    print('False')

