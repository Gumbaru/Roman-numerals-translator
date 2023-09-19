"""
Title : Programme de division eucledienne avec chiffre romain

Version : 1.0 

Author : Elias De Bernardo

Date : 16/09/2023 

"""
from function import *

#Entrée utilisateur pour definir la valeur à convertir
n = int(input("Rentrez votre numérateur: "))

#Creation de variables utile a la fonction "convertir_en_romain()""
nombre_de_millier = n // 1000
nombre_romain = nombre_de_millier * "M"
reste = n - (nombre_de_millier * 1000)


if nombre_de_millier < 1:
    print("La valeur est inférieure à un donc n'est pas divisble par 1000", )
    print("Le reste est =", reste)
else:
    print("La valeur est supérieure à un et =", nombre_romain)
    print("Le reste est =", reste)

if reste > 0:
    chiffres_romains_reste = convertir_en_romain(reste)
    nombre_romain += chiffres_romains_reste

print("Le nombre romain est =", nombre_romain)

