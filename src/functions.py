# src/functions.py

def add(a, b):
    """
    Soma dois números.
    
    Args:
        a (int): O primeiro número.
        b (int): O segundo número.
        
    Returns:
        int: A soma dos dois números.
    """
    return a + b

def subtract(a, b):
    """
    Subtrai o segundo número do primeiro.
    
    Args:
        a (int): O primeiro número.
        b (int): O segundo número.
        
    Returns:
        int: A diferença entre os dois números.
    """
    return a - b

def divide(a, b):
    """
    Divide o primeiro número pelo segundo.
    
    Args:
        a (int or float): O numerador.
        b (int or float): O denominador.
        
    Returns:
        float: O resultado da divisão.
        
    Raises:
        ValueError: Se o denominador for zero.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b
