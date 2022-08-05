# -*- coding: utf-8 -*-
"""
Created on Thu Aug  4 18:37:31 2022

@author: Fabricio
"""

def readint (prompt, min, max):
    
    try:
        x = int(input(prompt))
    
        if x >= min and x <= max:
            return (x)
        else:
            print("El valor no está en el rango permitdo") 
            v = readint("Ingrese un número desde -10 a 10: ", -10, 10)
    
    except ValueError:
        
        print("error en el ingreso")
        v = readint("Ingrese un número desde -10 a 10: ", -10, 10)
        
v = readint("Ingrese un número desde -10 a 10: ", -10, 10)


print("El número es: ", v)    