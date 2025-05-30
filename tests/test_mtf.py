import pytest
from mtf import move_to_front

def test_mtf_simple_case():
    lista = [0, 1, 2, 3, 4]
    secuencia = [2, 2, 2]
    costo_total, historial = move_to_front(lista, secuencia)
    assert costo_total == 5
    assert historial[0]["lista_despues"][0] == 2  
    assert historial[1]["lista_despues"][0] == 2
    assert historial[2]["lista_despues"][0] == 2
