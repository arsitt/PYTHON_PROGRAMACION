"""
Dada una cadena de texto, convertir cada letra a su código ASCII.
Con esto creamos un número que llamaremos total_1.
Cambiar todos los número '7' por '1' y a ese numero le llamaremos total_2

"""

def charcodde(cadena): # Creamos una función que coge una cadena como argumento
    total_2 = [] # Creamos una lista vacia
    for elem in cadena: # Por cada elemento en la cadena (Que es C y A)
        tmp = str(ord(elem)) # Reemplaza el elemento por un caracter ascii y lo convierte en str
        total_2.append(tmp) # Agrega los str en total_2 (una lista con strings)

    numero_1 = ''.join(total_2) # Añade los elementos de la lista a un str vacio.
    numero_2 = numero_1.replace('7','1') # Reemplaza los caracteres de 7 por 1 

    return int(numero_1) - int(numero_2) # Cambia la cadena a un entero y las resta


print(charcodde("CA"))