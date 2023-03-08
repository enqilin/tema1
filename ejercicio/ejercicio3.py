"""
Dadas dos listas, debes generar una tercera con todos los elementos que se repitan en ellas,
pero no debe repetirse ningún elemento en la nueva lista:

lista_1 = ["h",'o','l','a',' ', 'm','u','n','d','o']

lista_2 = ["h",'o','l','a',' ', 'l','u','n','a']
"""



lista_1 = ["h",'o','l','a',' ', 'm','u','n','d','o']
lista_2 = ["h",'o','l','a',' ', 'l','u','n','a']


def lista_3(lista1 , lista2):
    lista=[]
    for elemento in lista2:
        if elemento in lista1 and elemento not in  lista:
            lista.append(elemento)
            
        else:
            pass
    return lista

if __name__=="__main__":
    lista_3(lista_1, lista_2)