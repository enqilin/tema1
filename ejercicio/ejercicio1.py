"""Al realizar una consulta en un registro hemos obtenido una cadena de texto corrupta al revés.
Al parecer contiene el nombre de un alumno y la nota de un exámen.
¿Cómo podríamos formatear la cadena y conseguir una estructura como la siguiente?
Nombre Apellido ha sacado un Nota de nota.
Ayuda
Para voltear una cadena rápidamente utilizando slicing podemos utilizar un tercer índice -1: cadena[::-1]
cadena = "zeréP nauJ,01"
"""



cadena ="zeréP nauJ,01"



class Alumno:

    def __init__(self, caden):
        self.caden=caden
        
        lista=[]
        lista= self.caden.split(",")
        nota=lista[1]
        nombre=lista[2]
        self.nota=nota
        self.nombre=nombre

    def __str__(self):
        return "{} ha sacado un {} de nota".format(self.nombre,self.nota)
