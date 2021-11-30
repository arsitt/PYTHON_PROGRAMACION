class Base(): #Definimos la clase llamada 'Base'
    datos = [] #Esto es una propiedad de la clase 'Base'


class Hijo1(Base): #Definimos una clase llamada Hijo1 y le metemos de atributo 'Base'
    def __init__(self, elemento): #__init__ ejecuta lo que tengas debajo cuando instancias una clase
        self.datos.append(elemento)
    def datos_base(self):
        return super().datos


class Hijo2(Base): # Definimos una clase llamada Hijo2 y le metemos de atributo la clase 'Base'
    def __init__(self,elemento):
        self.datos.append(elemento) 
    def __str__(self) -> str:
        return 'Soy el hijo 1'


h1 = Hijo1('Hijo1')
h2 = Hijo2('Hijo2')

print(h1)
print(h2)

print(h1)
print(h2.datos)