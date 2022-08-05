# -*- coding: utf-8 -*-
"""
Created on Tue Aug  2 20:17:53 2022

@author: Fabricio
"""

def fibonacci(n):
    a = 0
    b = 1
    c = 0
    while a < n:
        print(a, end=' ')
        c = a
        a = b
        b = a + c    
fibonacci(20)