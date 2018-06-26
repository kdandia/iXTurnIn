#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 17:42:23 2018

@author: karinadandia
"""
    
 #%%
#PROBLEM 1:FIZZBUZZ 
numbers = 101
n = 1 
while n < numbers:
        if (n%3 == 0) and (n%5 == 0):
            print('FizzBuzz')
            n += 1
        elif (n%3 == 0):
            print('Fizz')
            n += 1
        elif (n%5 == 0):
            print('Buzz')
            n += 1
        else: 
            print(n)
            n += 1
            
    
 #%%         
#PROBLEM 2:INTEGER TO ROMAN NUMERALS CONVERTER
def int_to_roman(x):
        roman = '' #empty string    
        rnumeral = [ [1000, 'M'], [900, 'CM'], [500, 'D'], [400, 'CD'], [100, 'C'],
                    [90, 'XC'], [50, 'L'], [40, 'XL'], [10, 'X'], [9, 'IX'], 
                    [5, 'V'], [4, 'IV'], [1, "I"] ]
        while x > 0 :
            for [i, r] in rnumeral:
                while x >= i:
                    roman+=r
                    x-=i
        return roman
    
    
 #%%
#PROBLEM 3:ROT13
import string
    
plaintext = "abcdefghijklmnopqrstuvwxyz"
alphabet = string.ascii_lowercase

for letter in plaintext:
    plainnum = alphabet.find(letter) #find index
    cnum = ((plainnum + 13) % 25) #cipher alphabet index
    cletter = alphabet[cnum] 
    print(cletter)

    

    
    
    