from src.calculadora import restar, sumar


def test_sumar_dos_numeros():
    assert sumar(2, 3) == 5


def test_sumar_numeros_negativos():
    assert sumar(-4, -6) == -10


def test_restar_dos_numeros():
    assert restar(10, 4) == 6

