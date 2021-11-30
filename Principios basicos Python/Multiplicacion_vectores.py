""" v1 = [1,2,3,4]
v2 = [7,8,9,23]
total = 0

for x in range (len(v1)):
# Importante: el len del bucle sirve para ir pillando dígito a dígito de las 2 variables.

    total+=v1[x]*v2[x]
# La funcion total dentro de el bucle es un acumulador que va sumando la multiplicacion de cada elemento en la lista(v1 y v2) por orden (gracias a el len de arriba) en la variable total, en este caso v1[1]*v2[1],v1[2]*v2[2],etc... 
print(total)    
# Aqui imprimimos la variable total la cual tiene la acumulación de la multiplicación """

origen = [1,2,3,4,5,'Jose','Alan','Fernando']
numeros = []
alumnos = []

for x in origen:
    if type(x) == str:
        alumnos.append(x)
    else:
        numeros.append(x)
print(origen)
print(alumnos)
print(numeros)


