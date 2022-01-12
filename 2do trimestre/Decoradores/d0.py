def suma(*args):
    lista = []
    if type(*args) == type(lista):
        suma_de = sum(*args)
        return suma_de
    else:
        pass

print(suma([2,2,6]))