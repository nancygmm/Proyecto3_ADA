import pytest
from imtf import improved_move_to_front

def test_imtf_no_lookahead_move():
    lista = [0, 1, 2, 3, 4]
    secuencia = [2, 0, 1]
    costo_total, historial = improved_move_to_front(lista, secuencia)
    assert historial[0]["lista_despues"] == [0, 1, 2, 3, 4]  

def test_imtf_with_lookahead_move():
    lista = [0, 1, 2, 3, 4]
    secuencia = [2, 1, 2]
    costo_total, historial = improved_move_to_front(lista, secuencia)
    assert historial[2]["lista_despues"][0] == 2
