def dividir(a,b):
    resultado = None
    try:
        #Lista de instrucciones
        resultado = a/b
    
    except ZeroDivisionError: #Esto lo muestra si hay un fallo en la división
        print("Se ha producido un error en la división")
    
    except TypeError: #Esto es un tipo de error.
        print("Solo se pueden dividir datos númericos")
    
    else: 
        print("Esta es la parte else")
    
    finally:
        print("Esto es el finally")
    
    return resultado