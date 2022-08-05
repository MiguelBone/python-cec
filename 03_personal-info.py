# -*- coding: utf-8 -*-
"""
Created on Thu Jul 28 19:23:48 2022

@author: Fabricio
"""

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = int(input("Ingrese su edad: "))
ciudad = input("Ingrese su ciudad de residencia: ")
space = " "

if edad >= 0  and edad <11:
    print(nombre + space + apellido + space + "es un niño")
else:
    if edad >=11 and edad < 18:
        print(nombre + space + apellido + space + "es un adolescente")
    else:
        if edad >= 18 and edad < 65:
            print(nombre + space + apellido + space + "es un adulto")
        else:
            print(nombre + space + apellido + space + "es un adulto mayor")
            
#print("Nombre: " + nombre + space + apellido + space + "edad: " + edad + space + "Ciudad de residencia: "+ ciudad)