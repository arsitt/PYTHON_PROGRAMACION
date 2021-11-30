class Persona():
    #Constructor de clase
    def __init__(self, nombre, edad, dni):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni
        
    #Funciones sobre la clase

    def mostrar(self): #Esta función nos muestra los atributos de la clase.
        print(self.nombre)
        print(self.edad)
        print(self.dni)

    def mayor(self): #Aqui tenemos la función que nos devuelve 1 si es mayor de 18 años y 0 si es menor de edad.
        if self.edad > 18:
            print(1)
        else: 
            print(0)

alumno1 = Persona('Alejandro', 20, '54438089X')

alumno1.mostrar()
alumno1.mayor()


    
