# Crea una clase llamada **Cuenta** que tendrá los siguientes atributos: 
# - titular (que es una persona) y saldo (puede tener decimales). El titular será obligatorio y la saldo es opcional. Construye los siguientes métodos para la clase:

# - Un constructor, donde los datos pueden estar vacíos.
# - Los setters y getters para cada uno de los atributos. El atributo no se puede modificar directamente, sólo ingresando o retirando dinero.
# - mostrar(): Muestra los datos de la cuenta.
# - ingresar(saldo): se ingresa una saldo a la cuenta, si la saldo introducida es negativa, no se hará nada.
# - retirar(saldo): se retira una saldo a la cuenta. La cuenta puede estar en números rojos.

class Cuenta():
    def __init__(self,nombre,saldo):
        self.nombre = nombre
        self.saldo = False
    
    def datoscuenta(self):
        print(self.nombre)
        print(self.saldo)
    
    def ingresar(self):
        ingreso = int(input('¿Cuanto dinero desea ingresar?: '))
        if ingreso > 0:
            print('Correcto! El saldo actual de su cuenta es: ')
            print(ingreso + self.saldo)
        else:
            pass
        
    
    def retirar(self):
        retiro = int(input('¿Cuanto dinero desea retirar?: '))
        print('Retiro realizado! El saldo actual de su cuenta es: ')
        print(self.saldo - retiro)



    
c1 = Cuenta('Alejandro',400)

# c1.ingresar() 
c1.retirar()