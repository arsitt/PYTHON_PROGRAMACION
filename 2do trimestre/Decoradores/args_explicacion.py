#Vamos a hacer una suma con *args como parametro

def sumar(*args):
    print(args) #Si lo imprimes sin * antes de args te da una tupla
    print(*args) #Con el * antes de args te los desempaqueta

print(type(sumar(4,5,6)))

