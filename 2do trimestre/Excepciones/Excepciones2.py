def dividir(a,b):
    resultado = None
    try:
        #Lista de instrucciones
        resultado = a/b
    
    except (ZeroDivisionError, TypeError) as e: #Ahora tenemos un paquete con los 2 errores.
        print("Se ha producido un error en la división")
        print(type(e).__name__) #Esta linea nos da el tipo de error que ha sido
        print(e)
    
    else: 
        print("Esta es la parte else")
    
    finally:
        print("Esto es el finally")
    
    return resultado

print(dividir(0,0))