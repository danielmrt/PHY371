# -*- coding: utf-8 -*-
"""
Created on Thu Sep 04 09:22:40 2014

@author: danie_000
"""

#Excercise
#A ball is dropped from a tower of height h with initial velocity zero. Write a program that asked the user
#To enter the heigh in meters of the tower, and then calculates and prints the time the ball takes until it
#hits the ground. Ignore the air resistance. ( Try to write a function for this task)
# 1/2 at**2 = h
# t = sqrt(2h/a)

import math as mt
print ('Welcome to Falling Time Calculator (FTC) ')
h = float(raw_input("Insert the Height for discover the time: "))
g=9.81 #Just for make it easy if you want to change the value
def height(h): return  mt.sqrt(2*(h/g)) #Simple answer, using mt instead the math for make it easy.
    
print height(h)# Printing the result
