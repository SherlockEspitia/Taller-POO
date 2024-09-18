class Animal:
    '''
    Define una clase "Animal" que tenga como propiedades "nombre" y "edad". 
    También debe tener un método "hacer_ruido" que muestre un mensaje genérico.
    '''
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def hacer_ruido(self):
        return 'Brrrr...'

class Perro(Animal):
    '''
    Crea una clase "Perro" que extienda de la clase "Animal" y que tenga como propiedad adicional "raza". 
    El método "hacer_ruido" de esta clase debe mostrar un ladrido.
    '''
    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, edad)
        self.raza = raza
    
    def hacer_ruido(self):
        return 'Woof'

class Gato(Animal):
    '''
    Crea una clase "Gato" que extienda de la clase "Animal" y que tenga como propiedad adicional "pelaje". 
    El método "hacer_ruido" de esta clase debe mostrar un maullido.
    '''
    def __init__(self, nombre, edad, pelaje):
        super().__init__(nombre, edad)
        self.pelaje = pelaje
    
    def hacer_ruido(self):
        return 'Miau'            