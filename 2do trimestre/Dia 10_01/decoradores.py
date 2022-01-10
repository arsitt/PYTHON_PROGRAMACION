# """"""
# Son funciones que admiten funciones como parametros
# Devuelven Funciones
# """"""
def mi_decorador(funcion_a_decorar):
    def envoltura(*args,**kwargs): #El args es una lista de valores y el kwargs es una lista de valores clave valor, esto lo hacemos para que coja los argumentos de suma.
        print("Este es el inicio de la funcion ----")
        c = funcion_a_decorar(*args,**kwargs)
        print(c)
        print("---- Este es el final de la función")
    return envoltura

@mi_decorador
def saludar():
    print("Hola mundo!")

# saludar() #Asi ejecuta mi_decorador y saludar, pasando el parametro saludar como funcion_a_decorar en mi_decorador
# resp = mi_decorador(saludar) 
# resp() # Esta variable ejecuta las 2 funciones que le hemos puesto pero gracias al @mi_decorador llamamos a la función y ejecuta la función saludar como parametro a decorar en esta

@mi_decorador
def sumar(a,b):
    return a + b

sumar(1,2)
# def restar(a,b):
#     return a - b 

    