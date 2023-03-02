"""Realiza una función separar(lista) que tome una lista de números enteros y devuelva dos listas ordenadas. 
La primera con los números pares y la segunda con los números impares.
Por ejemplo:
pares, impares = separar([6,5,2,1,7])
print(pares)
print(impares)
[2, 6]

[1, 5, 7]

Sugerencia

Para ordenar una lista automáticamente puedes utilizar el método .sort()."""
numero=[6,5,2,1,7]

def separar(lista):
    lista2=[]
    lista1=[]
    for n in lista:
        if n%2==0:
            lista2.append(n)
            lista2.sort()
        else:
            lista1.append(n)
            lista1.sort()            
    print("los números impares son: ", lista1,"los números pares son: ",lista2)

separar(numero)