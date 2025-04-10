# polimorfismo

class Triangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def calcArea(self):
        area = self.base * self.altura / 2
        return area

class Quadrado:
    def __init__(self, lado):
        self.lado = lado
    
    def calcArea(self):
        area = self.lado * self.lado
        return area
    
meuTriangulo = Triangulo(4,5)
meuQuadrado = Quadrado(5)

print(meuTriangulo.calcArea())
print(meuQuadrado.calcArea())
