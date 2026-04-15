class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print("Hola, mi nombre es", self.nombre)


persona1 = Persona("Arlet", 26)

persona1.saludar()

print(persona1.edad)