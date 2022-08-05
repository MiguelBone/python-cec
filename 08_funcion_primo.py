# -*- coding: utf-8 -*-
"""
Created on Mon Aug  1 20:21:29 2022

@author: Fabricio
"""

def isPrime(num):
    contador = 0
    for index in range(2,num):
        if num % index == 0:
            contador=contador + 1
            print(index)
    if contador == 1:        
       return index
                    
for i in range (1,20):
    if isPrime(i+1):
        print(i+1,end=" ")
print()        
    