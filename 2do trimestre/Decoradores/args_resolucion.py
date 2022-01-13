# Aqui vamos a pasar una cadena a numeros enteros con *args

def sumar(*args):
    lista = [] #Creamos una lista vacia para contener los numeros
    for cadena in args: # Esto significa que por cada elemento en args, (aqui solo tenemos una cadena, por eso el nombre)
        for elem in cadena.split(","): # Lee todos los elementos de la cadena y 
            if elem.isdigit():
                lista.append(int(elem))
    for i in lista:
        print(i)

sumar("1,2,3","9,8,7")

