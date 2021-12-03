    # Constructor que admita numerador y denominador
    # Constructor sin parámetros
    # Métodos getters y setters
    # Suma, Resta, Multiplicación y División

from fractions import Fraction
import fractions


class Racional():
    # Aqui tenemos el init, que sirve para crear el numerador y el denominador
    def __init__(self, numerador, denominador):
        self.numerador = numerador
        self.denominador = denominador
    
    ##SETTERS#

    def setDenominador(self):
        if self.denominador == 0:
            print('Un denominador no puede ser 0.')
        else:
            return self.denominador
        

    ##GETTERS##
    def getNumerador(self):
        return print(self.numerador)
    
    def getDenominador(self):
        return 
    
    def getFraccion(self):
        fraccion = print(self.numerador, '/', self.denominador)
        return fraccion
    
    ##FUNCIONES##
    def multiplicar(self):
        multiply = self.numerador * self.denominador
        return multiply
    
    def dividir(self):
        divide = self.numerador / self.denominador
        return divide
    
    def sumar(self):
        add = self.numerador + self.denominador
        return add
    
    def restar(self):
        substract = self.numerador - self.denominador
        return substract
    pass

c1 = Racional(4,0)
c2 = Racional(2,2)

c1.getFraccion()
c1.getNumerador()
c1.getDenominador()

