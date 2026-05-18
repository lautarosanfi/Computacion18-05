def sumar(a, b):
    """Devuelve la suma de dos numeros."""
    return a + b


def restar(a, b):
    """Devuelve la resta entre dos numeros."""
    return a - b

def multiplicar(a, b):
    """Devuelve el producto de dos numeros."""
    return a * b

def dividir(a, b):
    """Devuelve la division entre dos numeros."""
    if b == 0:
        raise ValueError("No se puede dividir por cero.")
    return a / b