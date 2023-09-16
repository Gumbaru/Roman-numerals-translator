"""
Title : Module de fonction qui est utilisé avec le main (main.py)

Version : 1.0 

Author : Aymeric 

Date : 16/09/2023 

"""
#Declaration de fonction avec un parametres notée
def convertir_en_romain(reste):

    #Liste de chiffre romain (chiffre classique => chiffre romain)
    val_romains = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
    ]
    
    chiffres_romains = ""

    #Parcours la liste par ordre decroissant, puis tant que le reste est superieur ou egal a la valeur actuelle
    #il incremente la reste en chiffre romain puis decremente la valeur est chiffre "normal"
    for valeur, symbole in val_romains:
    
        while reste >= valeur:
      
            chiffres_romains += symbole
           
            reste -= valeur

    return chiffres_romains