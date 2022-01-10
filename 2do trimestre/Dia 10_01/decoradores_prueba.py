def decorador(funcion):
    def envoltura(*args):
        lista = []
        if not type(args) == tuple:
            lista = tuple(args)
            return funcion(args)
        else:
            return funcion(args)
            # for i in args:
            #     lista.append(i)
            #     print(lista)
    return envoltura

@decorador
def suma(*args):
    return sum(args)

print(suma("1,2,3"))