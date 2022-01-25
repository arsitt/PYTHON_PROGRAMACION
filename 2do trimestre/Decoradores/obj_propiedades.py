from datetime import date

class Persona():
    def __init__(self, nombre, dni, fecha_nac):
        self.__nombre = nombre
        self.__dni = dni
        self.__fecha_nac = fecha_nac
    
    def get_nombre(self):
        return self.__nombre

    def set_nombre(self):
        self.__nombre = nombre

    def get_dni(self):
        return self.__dni
    
    def set_dni(self):
        self.__dni

    @property
    def fecha_nacimiento(self):
        return self.__fecha_nac
    
    @fecha_nacimiento.setter
    def fecha_nac(self, fecha):
        self.__fecha_nac= fecha


alumno1 = Persona('Alejandro','54438089X', '15/06/2021')

print(alumno1.fecha_nacimiento)