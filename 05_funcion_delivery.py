# -*- coding: utf-8 -*-
"""
Created on Mon Aug  1 19:04:33 2022

@author: Fabricio
"""

def delivery(barrio,calle,casa):
    print("La dirección de su entrega de su pedido es: ", "Barrio", barrio, calle, casa)
    
barrio = input("Cuál es el barrio: ")
calle = input("Cuál es el nombre de la calle: ")    
casa = input("Cuál es el número de la casa: ") 
delivery(barrio,calle,casa)