""""
Crea una clase NIF que se usará para mantener DNIs con su correspondiente letra.

Los atributos serán el número de DNI (entero largo) y la letra que le corresponde.

La clase dispondrá de los siguientes métodos:

Constructor predeterminado que inicialice el nº de DNI a 0 y la letra a espacio en
blanco (será un NIF no válido).

Constructor que reciba el DNI y establezca la letra que le corresponde.

Accedentes y mutador para el número de DNI (que ajuste automáticamente la letra).

leer(): que pida el número de DNI (ajustando automáticamente la letra)

Método que nos permita mostrar el NIF (ocho dígitos, un guión y la letra en
mayúscula; por ejemplo: 00395469-F)

La letra se calculará con un método auxiliar (privado) de la siguiente forma:
se obtiene el resto de la división entera del número de DNI entre 23 y se usa la
siguiente tabla para obtener la letra que corresponde:

0 - T
7 - F
1 - R
8 - P
2 - W
9 - D
3 - A
10 - X
4 - G
11 - B
5 - M
12 - N
6 – Y
13 – J
14 - Z
21 - K
15 - S
22 – E
16 - Q
17 - V
18 - H
19 - L
20 – C

"""

class DNI():
    __letras = {0 : 'T', 7 : 'F', 1 : 'R', 8 : 'P', 2 : 'W', 9 : 'D', 3 : 'A', 10 : 'X', 4 : 'G', 11 : 'B', 5 : 'M', 12 : 'N', 6 : 'Y', 13 : 'J', 14 : 'Z', 21 : 'K', 15 : 'S', 22 : 'E', 16 : 'Q', 17 : 'V', 18 : 'H', 19 : 'L', 20 : 'C' }
    def __init__(self,num, letra) -> None:
        self.__num = num
        self.__letra = self.set_letra()
        
    def comprobacion(self):
        self.__num = 245864234

    @property
    def number(self):
        return self.__num
    
    @number.setter
    def numset(self, num):
        self.__num = num
    
    def set_letra(self):
        # TODO: Hacer comprobacion si es entero
        num23 = self.__num%23
        letra = self.__letras.get(num23)
        return letra
    
    def resultado(self):
        num_letra = str(self.__num) + '-' + self.__letra
        return num_letra

p = DNI(24534443,'')


print(p.comprobacion())

