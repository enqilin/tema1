"""Realiza un programa que cumpla el siguiente algoritmo utilizando siempre que sea posible operadores en asignación:
Guarda en una variable numero_magico el valor 12345679 (sin el 8)
Lee por pantalla otro numero_usuario, especifica que sea entre 1 y 9
Multiplica el numero_usuario por 9 en sí mismo
Multiplica el numero_magico por el numero_usuario en sí mismo
Finalmente muestra el valor final del numero_magico por pantalla """

import sys
numero_magico=12345679
def numero_usuario():
     numero=input("Introduce un número de 1~9: ")
     try:
          numero=int(numero)
          if 1<=numero<=9:
               return numero
          else:
               pass
     except:
          rasise ValueError("El carácter no es válido", file=sys.stderr)

def calculo(numero_usuario):
     multi=numero_usuario*9
     final=multi*numero_magico
     return final
     



    
          