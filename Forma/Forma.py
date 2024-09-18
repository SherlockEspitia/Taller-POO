from math import PI, pow 

class Forma:
    '''
    Define una clase "Forma" que tenga como propiedades "ancho" y "alto". 
    También debe tener un método "calcular_area" que devuelva el área de la forma.
    '''
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto
    
    def calcular_area(self):
        return self.alto*self.ancho

class Rectangulo(Forma):
    '''
    Crea una clase "Rectangulo" que extienda de la clase "Forma" 
    y que tenga como método adicional "calcular_perimetro" que devuelva el perímetro del rectángulo.
    '''
    def __init__(self, ancho, alto):
        super().__init__(ancho, alto)
    
    def calcular_perimetro(self):
        return 2*self.alto + 2*self.ancho

class Circuferencia(Forma):
    '''
    Crea una clase "Circulo" que extienda de la clase "Forma" 
    y que tenga como método adicional "calcular_circunferencia" que devuelva la circunferencia del círculo.
    '''
    def __init__(self, radio):
        self.radio
    
    def calcular_area(self):
        return PI*pow(self.radio,2)
    
    def calcular_circunferencia(self):
        return 2*PI*self.radio