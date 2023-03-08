import unittest
from ejercicio import ejercicio1 as E1
from ejercicio import ejercicio2 as E2
from ejercicio import ejercicio3 as E3
from ejercicio import ejercicio4 as E4
from ejercicio import ejercicio6 as E6
from ejercicio import ejercicio7 as E7
from ejercicio import descomposion as de



class TestEjercicio(unittest.TestCase):

    def test_ejercicio1(self):
        nombre_nota= E1.Alumno("zeréP nauJ,01")
        self.assertEqual(nombre_nota,"Juan Péraz ha sacado 10 de nota")

    def test_ejercicio2(self):
        calculo_numero_ususario=E2.calculo
        self.assertEqual(calculo_numero_ususario,E2.calculo)

    def test_ejercicio3(self):
        lista= E3.lista_3
        self.assertEqual(lista,['h','o','l','a',' ','u','n'])

    def test_ejercicio4(self):
        orden=E4.orden
        self.assertEqual(orden,[-2,1,5])
    def test_ejercicio6(self):
        separar=E6.separar
        self.assertEqual(separar,"los números impares son: [1,5,7] los números pares son: [2,6]")
    def test_ejercicio7(self):
        agregar=E7.agregar_una_vez
        self.assertEqual(agregar,[1, 5, -2, 10])

    def test_descomposion(self):
        descomposion=de.descomposion(3647)
        self.assertEqual(descomposion,"2))




