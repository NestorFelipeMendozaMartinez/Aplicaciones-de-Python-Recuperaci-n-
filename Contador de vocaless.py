def contar_vocales(palabra):
    vocales = "aeiouAEIOU"
    return sum(1 for letra in palabra if letra in vocales)

print(contar_vocales("Hola Mundo"))  # Salida: 4