import helpers
from ejercicio import ejercicio1 as E1
from ejercicio import ejercicio2 as E2
from ejercicio import ejercicio3 as E3
from ejercicio import ejercicio4 as E4
from ejercicio import ejercicio6 as E6
from ejercicio import ejercicio7 as E7
from ejercicio import descomposion as dc


def iniciar():
    while True:

        print("================")
        print("[1] Ejercicio 1 ")
        print("[2] Ejercicio 2 ")
        print("[3] Ejercicio 3 ")
        print("[4] Ejercicio 4 ")
        print("[5] Ejercicio 5 ")
        print("[6] Ejercicio 6 ")
        print("[7] Ejercicio 7 ")
        print("[8] Ejercicio 8 ")
        print("================")

        option= input ("> ")

        helpers.limpiar_pantalla()

        if option==1:
            print("Ejercicio 1\n")
            numero1=E1.Alumno
            print(numero1)
        
        elif option==2:
            print("Ejercicio 2\n")
            numero2=E2.calculo
            print(numero2)

        elif option==3:
            print("Ejercicio 3 \n")
            numero3=E3.lista_3
            print(numero3)
        
        elif option==4:
            print("Ejercicio 4 \n")
            numero4=E4.orden
            print(numero4)

        elif option==5:
            print("Ejercicio 5 \n")
            numero5=dc.descomposion
            print(numero5)

        elif option==6:
            print("Ejercicio 6 \n")
            numero6=E6.separar
            print(numero6)

        elif option==7:
            print("Ejercicio 7 \n")
            numero7=E7.agregar_una_vez
            print(numero7)
        elif option==8:
            print("salir de ejercicio")
            break
        input("\nPresiona Enter para continuar...")