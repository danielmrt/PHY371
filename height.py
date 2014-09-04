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
h = float(raw_input("Insert the Height for discover the time: "))
g=9.8
def height(h): return  mt.sqrt(2(h/g))
    
print height(h)
