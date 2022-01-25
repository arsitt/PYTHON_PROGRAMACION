class Coche():
    #Constructor que crea instancia de la clase
    def __init__(self, color, marca, modelo, num_p, matricula)-> str: #Variables vacias
        self.__color = color
        self.__marca = marca
        self.__modelo = modelo
        self.__num_p = num_p
        self.__matricula = matricula
        self.__arrancado = False
    #__str__ que nos va a devolver los datos formateados como queremos
    def __str__(self) -> str:
        return f'Color: {self.__color}\nMarca: {self.__marca}\nModelo: {self.__modelo}\nNúmero de puertas: {self.__num_p}\nMatricula: {self.__matricula}\n'
    
    #Getters de la clase(como propiedades)
    @property
    def color(self):    
        return self.__color
    
    @property
    def marca(self):
        return self.__marca
    
    @property
    def modelo(self):
        return self.__modelo

    @property
    def num_p(self):
        return self.__num_p

    @property
    def matricula(self):
        return self.__matricula
    
    #Setters de la función

    @color.setter
    def color(self, color):
        self.__color = color
        return self.__color

    @marca.setter
    def marca(self, marca):
        self.__marca = marca
        return self.__marca

    @modelo.setter
    def modelo(self, modelo):
        self.__modelo = modelo
        return self.__modelo

    @num_p.setter
    def num_p(self, num_p):
        self.__num_p = num_p
        return self.__num_p

    @matricula.setter
    def matricula(self, matricula):    
        self.__matricula = matricula
        return self.__matricula

''''
Estas lineas de codigo sobran ya que hacen funciones que no se nos han pedido

    def arrancar(self):
        print("Arrancando el coche...")
        self.arrancado = True
    
    def ver_estado(self):
        if self.arrancado == False:
            print("El coche esta apagado")
        else:
            print("El coche esta encendido")

'''

laguna = Coche( "Blanco", "Renault", "Laguna", "5", "22948K")
print(laguna)

tesla = Coche("Negro", "Tesla", "Model Y", "3", "36784T")
print(tesla)

beamer = Coche("Rojo", "BMW", "M3", "5", "90345D")
print(beamer)