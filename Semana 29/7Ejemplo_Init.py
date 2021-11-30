class Persona():
    def __init__(self, nombre, edad, dni) -> None:
            self.nombre = nombre
            self.edad = edad
            self.dni = dni

    
p1 = Persona('Alejandro', 20, '54438089X')
print(p1.nombre, p1.dni)