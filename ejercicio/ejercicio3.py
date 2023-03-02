"""
Dadas dos listas, debes generar una tercera con todos los elementos que se repitan en ellas,
pero no debe repetirse ningún elemento en la nueva lista:

lista_1 = ["h",'o','l','a',' ', 'm','u','n','d','o']

lista_2 = ["h",'o','l','a',' ', 'l','u','n','a']
"""



lista_1 = ["h",'o','l','a',' ', 'm','u','n','d','o']
lista_2 = ["h",'o','l','a',' ', 'l','u','n','a']

def lista_3(lista_1 , lista_2):
    lista=[]
    for elemento in lista_2:
        if elemento in lista_1:
            lista.append(lista_1)
        else:
            pass
        return lista