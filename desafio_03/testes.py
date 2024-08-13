import pytest
from main import maior_soma_subarray

class TestClass:
    def test_lista_so_com_numeros_inteiros(self):
        """Testa com lista de números positivos"""
        lista_de_inteiros = [1,2,3,4,5,6,7,8,9,10]
        subarray, maior_numero = maior_soma_subarray(lista_de_inteiros)

        assert subarray == [1,2,3,4,5,6,7,8,9,10]
        assert maior_numero == 55

    def test_lista_so_com_numeros_negativos(self):
        """Testa com lista de números negativos"""
        lista_de_negativos = [-1,-2,-3,-4,-5,-6,-7,-8,-9,-10]

        subarray, maior_numero = maior_soma_subarray(lista_de_negativos)
        assert subarray == [-1]
        assert maior_numero == -1

    def test_passando_lista_vazia(self):
        """Testa com lista vazia"""
        lista_de_negativos = []

        subarray, maior_numero = maior_soma_subarray(lista_de_negativos)
        assert subarray == []
        assert maior_numero == 0

    def test_lista_normal(self):
        """Testa com a lista com negativos e positivos"""
        lista_de_negativos = [-2,-3,4,-1,-2,1,5,-3]

        subarray, maior_numero = maior_soma_subarray(lista_de_negativos)
        assert subarray == [4,-1,-2,1,5]
        assert maior_numero == 7

    def test_lista_com_um_numero_inteiro(self):
        """Testa com a lista um unico número positivo"""
        lista_de_negativos = [2]

        subarray, maior_numero = maior_soma_subarray(lista_de_negativos)
        assert subarray == [2]
        assert maior_numero == 2

    def test_lista_com_zeros_e_positivos(self):
        """Testa com a lista um unico número negativo"""
        lista_de_negativos = [-2]

        subarray, maior_numero = maior_soma_subarray(lista_de_negativos)
        assert subarray == [-2]
        assert maior_numero == -2

    def test_lista_com_zeros_e_negativos(self):
        """Testa com a lista com zeros e negativos"""
        lista_de_negativos = [0, -2, 0, -5, 0, -1, 0, -2]

        subarray, maior_numero = maior_soma_subarray(lista_de_negativos)
        assert subarray == [0]
        assert maior_numero == 0