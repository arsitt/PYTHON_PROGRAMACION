class Base(): #Definimos la clase llamada 'Base'
    __nombre = None
    def __init__(self) -> None:
        self.datos = []#Aqui creamos una propiedad de la clase 'Base' llamada 'datos'


class Hijo1(Base): #Definimos una clase llamada Hijo1 y le metemos de atributo 'Base'
    def __init__(self, elemento):
        super().__init__() #LLama a la funcion __init__ del padre, el cual crea un datos[] en el self
        self.datos.append(elemento) #Añadimos elemento a datos, creado en self

class Hijo2(Base): #Definimos una clase llamada Hijo1 y le metemos de atributo 'Base'
    def __init__(self, elemento):
        super().__init__() 
        self.datos.append(elemento)

h1 = Hijo1('Hijo1') # Esto sera el elemento dentro de Hijo1
h2 = Hijo2('Hijo 2') # Esto sera el elemento dentro de Hijo2
h1.nombre

print(h1.datos) #Imprimimos la lista datos dentro de la variable h1, que contiene dentro la clase 'Hijo1'
print(h2.datos)