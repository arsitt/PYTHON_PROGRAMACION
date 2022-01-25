
class Square():
    #Constructor que crea instancia de la clase
    def __init__(self, base, altura) -> None:
        self.base = base
        self.altura = altura

    def area(self):
        area = self.base * self.altura
        return area
    
    def perimetro(self):
        perimetro = (2 * self.base) + (2 * self.altura) 
        return perimetro
        
s1 = Square(10,6)

print(s1.area())
print(s1.perimetro())

