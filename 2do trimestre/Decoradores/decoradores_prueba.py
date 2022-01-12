def decorador(funcion):
    def envoltura(*args): #Envoltura con el parametro args detras para que coja esos argumentos
        lista = [] # Lista vacia para comparar y rellenar
        strin = "" # String vacio para comparar
        for i in args: # Por cada elemento de la tupla args
            if type(i) == type(lista): # Se compara si el elemento es una lista ya
                do = funcion(i) # Si lo es, ejecuta la función sumar
                return do
            elif type(i) == type(strin):
                i = i.split(",")
                dd = funcion(i)
                return dd
    return envoltura

@decorador
def sumar(i):
    sumando = sum(i)
    return sumando

print(sumar("1,2,3"))



# Hacer una función suma a la que le pasemos una lista de elementos a sumar. Hacer un decorador que permita que pueda ser tanto una lista de números como una cadena de números separados por comas.
# Es decir.
# [1,2,3,4] y “1,2,3,4” darán la misma suma, que es 10