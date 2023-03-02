import os
import run
import ejercicio

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
        os.system("clear")
        if option==1:
            print("Ejercicio 1 \n")
            for numero1 in ejercicio/ejercicio1:
                print(numero1)
        
        elif option==2:
            print("Ejercicio  \n")
            for numero2 in ejercicio/ejercicio2:
                print(numero2)

        elif option==3:
            print("Ejercicio  \n")
            for numero2 in ejercicio/ejercicio3:
                print(numero2)
        
        elif option==4:
            print("Ejercicio  \n")
            for numero2 in ejercicio/ejercicio4:
                print(numero2)

        elif option==5:
            print("Ejercicio  \n")
            for numero2 in ejercicio/ejercicio5:
                print(numero2)

        elif option==6:
            print("Ejercicio  \n")
            for numero2 in ejercicio/ejercicio6:
                print(numero2)
        
        elif option==7:
            print("Ejercicio  \n")
            for numero2 in ejercicio/ejercicio7:
                print(numero2)
        elif option==8:
            print("salir de gestor")
            break
        input("\nPresiona Enter para continuar...")
