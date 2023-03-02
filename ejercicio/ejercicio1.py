"""Al realizar una consulta en un registro hemos obtenido una cadena de texto corrupta al revés.
Al parecer contiene el nombre de un alumno y la nota de un exámen.
¿Cómo podríamos formatear la cadena y conseguir una estructura como la siguiente?
Nombre Apellido ha sacado un Nota de nota.
Ayuda
Para voltear una cadena rápidamente utilizando slicing podemos utilizar un tercer índice -1: cadena[::-1]
cadena = "zeréP nauJ,01"
"""



cadenaa ="zeréP nauJ,01"



class Alumno:

    def __init__(self, cadena):
        self.cadena=cadena

    def slicing(self):
        lista=[]
        lista= cadena.split(",")
        nota=lista[1]
        nombre=lista[2]
        return nota, nombre

    def representar(self):
        return nombre,"ha sacado un ", nota , " de nota."
