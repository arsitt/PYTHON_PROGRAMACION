class Coche():
    #Constructor que crea instancia de la clase
    def __init__(self, color, marca, modelo, num_p, matricula):
        self.color = color
        self.marca = marca
        self.modelo = modelo
        self.num_p = num_p
        self.matricula = matricula
        self.arrancado = False

    def mostrar(self):
        mostrar = print( self.color, self.marca, self.modelo, self.num_p, self.matricula)
        return mostrar
    
    def arrancar(self):
        print("Arrancando el coche...")
        self.arrancado = True
    
    def ver_estado(self):
        if self.arrancado == False:
            print("El coche esta apagado")
        else:
            print("El coche esta encendido")

laguna = Coche( "Blanco", "Renault", "Laguna", "5", "22948K")

laguna.mostrar()
laguna.ver_estado()