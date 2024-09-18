class Persona:
    '''
    Define una clase "Persona" que tenga como propiedades "nombre", "apellido" y "edad". 
    También debe tener un método "obtener_nombre_completo" que devuelva el nombre completo de la persona.
    '''
    def __init__(self, nombre, apellido, edad):
        self.nombre, self.apellido, self.edad = nombre, apellido, edad
    
    def obtener_nombre_completo(self):
        return f'${self.nombre} ${self.apellido}'

class Estudiante(Persona):
    '''
    Crea una clase "Estudiante" que extienda de la clase "Persona" y que tenga como propiedad adicional "carrera". 
    El método "obtener_nombre_completo" de esta clase debe devolver el nombre completo del estudiante y su carrera.
    '''
    def __init__(self, nombre, apellido, edad, carrera):
        super().__init__(nombre, apellido, edad)
        self.carrera = carrera
    
    def obtener_nombre_completo(self):
        return f'${super().obtener_nombre_completo()} ${self.carrera}'

class Profesor(Persona):
    '''
    Crea una clase "Profesor" que extienda de la clase "Persona" y que tenga como propiedad adicional "materia". 
    El método "obtener_nombre_completo" de esta clase debe devolver el nombre completo del profesor y la materia que enseña.
    '''
    def __init__(self, nombre, apellido, edad, materia):
        super().__init__(nombre, apellido, edad)
        self.materia = materia
    
    def obtener_nombre_completo(self):
        return f'${super().obtener_nombre_completo()} ${self.materia}'