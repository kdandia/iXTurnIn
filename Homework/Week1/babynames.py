#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 11:00:47 2018

@author: karinadandia
"""
from collections import Counter

def babynames():
    
    girls = []
    boys = []
    
    years = range(1900, 2017)
    
    #loop to open all data files 
    for i in years:
        with open("data/names_{}.txt".format((i))) as f:
            line1 = f.readline().strip("\n") #take out enter at the end of each name
           
            boys.append((line1.split('|")[1])) #column 1 boy name
            girls.append((line1.split('|")[2])) #column 2 girl name
            
    #make a dictionary to count the number of names
    bdictionary = Counter(boys)
    gdictionary = Counter(girls)
    
    
    #accept user input for name 
    uinput = input("Insert the name you want to search").capitalize()
    
    if uinput in gdictionary:
        print("The name was popular {} times for girls and 0 times for boys".format(girls[]))
        
    if uinput in bdictionary:
        print("The name was popular 0 times for girls and {} times for boys".format(boys[]))
        
    if uinput not in gdictionary and not in bdictionary:
        print("This name was not popular for boys or girls")
        

babynames()