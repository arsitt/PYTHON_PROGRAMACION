from email.mime import base


class Square():
    #Constructor que crea instancia de la clase
    def __init__(self, base=0, altura=0) -> None: #Podriamos añadir que la base y la altura fuese por defecto 0
        self.__base = base #Variables privadas de la clase
        self.__altura = altura
    
    def __str__(self) -> None: #__str__ Para cuando hagas print del objeto te imprima el contenido de este
        return (f'Este rectangulo tiene una base de {self.__base}, una altura de {self.__altura}.\nEsto significa que su area será de {self.area()} y su perimetro será de {self.perimetro()}')

    #Podemos hacer Setters y Getters:

    #Getters como propiedades

    @property
    def base(self):
        return self.__base

    @property 
    def altura(self):
        return self.__altura
    
    #Setters

    @base.setter
    def base(self, base):
        self.__base = base
        return base
    
    @altura.setter
    def altura(self, altura):
        self.__altura = altura
        return altura

    #Métodos para el area y el perimetro.

    def area(self):
        area = self.__base * self.__altura
        return area
    
    def perimetro(self):
        perimetro = (2 * self.__base) + (2 * self.__altura) 
        return perimetro


""""

Ahora tenemos la base y la altura como propiedades de la clase y solo tendremos que llamarlas con s1.base o s1.altura para poder instanciar las propiedades, sin los parentesis

"""

s1 = Square(10,6)

print(s1)
s1.altura