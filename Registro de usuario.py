class Usuario:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def mostrar_info(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}"

usuario1 = Usuario("Ana", 25)
print(usuario1.mostrar_info())  # Salida: Nombre: Ana, Edad: 25