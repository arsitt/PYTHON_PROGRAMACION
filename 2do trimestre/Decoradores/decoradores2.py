from logging import exception


def son_enteros(funcion):
    def envoltura(*args):
        for i in args:
            if not type(i) is int:
                raise Exception('El numero no es entero')
        return funcion(*args)
    return envoltura

@son_enteros
def suma(*args):
    return sum(args)


#Multiplicacion de numeros enteros
# @son_enteros
# def multiplicacion(a,b):
#     return a*b

# resp = multiplicacion(2,6)
# print(resp)

resp = suma(2,3,4)
print(resp)