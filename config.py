import re
import os
import platform


def limpiar_pantalla():
    os.system('cls') if platform.system()=="Windows" else os.system('clear')

def leer_texto(longitud_min=0,longitud_max=20,mensaje=None):
    print(mensaje) if mensaje else  None
    while True:
        texto= inpur("> ")
        if len(texto)>=longitud_min and len(texto)<=longitud_max:
            return texto
        
