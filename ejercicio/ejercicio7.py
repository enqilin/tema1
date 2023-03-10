"""Realiza una función llamada agregar_una_vez(lista, el) que reciba una lista y un elemento.
La función debe añadir el elemento al final de la lista con la condición de no repetir ningún elemento.
Además si este elemento ya se encuentra en la lista se debe invocar un error de tipo ValueError que debes capturar y mostrar este mensaje en su lugar:

Error: Imposible añadir elementos duplicados => [elemento].
Cuando tengas la función intenta añadir los siguiente valores a la lista 10, -2, "Hola" y luego muestra su contenido.

Sugerencia

Puedes utilizar la sintaxis "elemento in lista"

elementos = [1, 5, -2]"""

elementos=[1 , 5 , -2]

def agregar_una_vez(lista, elemento):
    for i in elemento:
        
        try:
            if i not in lista:
                lista.append(i)
            else:
                pass
        except:
            raise ValueError("Error: Imposible añadir elementos duplicados => [elemento]. ")

        return print(lista)
            
if __name__=="__main__":
    agregar_una_vez(elementos,[10, -2 , "Hola"])