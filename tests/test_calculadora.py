from src.calculadora import restar, sumar, multiplicar, dividir


def test_sumar_dos_numeros():
    assert sumar(2, 3) == 5


def test_sumar_numeros_negativos():
    assert sumar(-4, -6) == -10


def test_restar_dos_numeros():
    assert restar(10, 4) == 6

def test_restar_numeros_negativos():
    assert restar(-5, -3) == -2

def test_multiplicar_dos_numeros():
    assert multiplicar(4, 5) == 20

def test_multiplicar_por_cero():
    assert multiplicar(7, 0) == 0

def test_dividir_dos_numeros():
    assert dividir(10, 2) == 5

def test_dividir_por_cero():
    try:
        dividir(5, 0)
        assert False, "Se esperaba una excepción ValueError"
    except ValueError as e:
        assert str(e) == "No se puede dividir por cero."

def test_dividir_numeros_negativos():
    assert dividir(-10, -2) == 5

def test_dividir_resultado_negativo():
    assert dividir(-10, 2) == -5

def test_dividir_resultado_decimal():
    assert dividir(7, 2) == 3.5