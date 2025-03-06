def calculadora(a, b, operacion):
    if operacion == '+':
        return a + b
    elif operacion == '-':
        return a - b
    elif operacion == '*':
        return a * b
    elif operacion == '/':
        return a / b
    else:
        return "Operación no válida"

print(calculadora(10, 5, '+'))  # Salida: 15