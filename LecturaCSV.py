# -*- coding: utf-8 -*-
"""
Created on Fri Aug  5 19:31:52 2022

@author: Fabricio
"""

import pandas as pd

titulos = pd.read_csv('data/titles.csv')
print(titulos.head(10))
print("\n"*2)
elenco = pd.read_csv('data/cast.csv')
print(elenco.head(10))
print(titulos[titulos.title.str.contains("Dracula")].sort_values("year"))
print(titulos[titulos.title.str.contains("war")].sort_values('year'))
print(titulos[titulos.title== "Dracula"].sort_values("year"))
print(titulos[titulos.title.str.contains("Dracula")].sort_values('year'))
print(titulos[titulos.title.str.contains("The Lord of the Rings")].sort_values('year'))
print(len(titulos[titulos.title.str.contains("The Lord of the Rings")].sort_values('year')))
print( elenco[elenco.character == "Superman"] )
print( len(elenco[elenco.character == "Superman"] ))
print( elenco[elenco.name == "Hugh Jackman"] )