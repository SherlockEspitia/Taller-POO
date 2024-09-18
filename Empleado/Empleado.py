class Empleado:
    '''
    Define una clase "Empleado" que tenga como propiedades "nombre", "apellido" y "sueldo". 
    También debe tener un método "calcular_salario_neto" que devuelva el salario neto del empleado, restando impuestos y otros descuentos.
    '''
    impuestos = 0.14
    deduciones = 0.14
    def __init__(self, nombre, apellido, sueldo):
        self.nombre, self.apellido, self.sueldo = nombre, apellido, sueldo

    def calcular_salario_neto(self):
        return self.sueldo*(1-self.deduciones-self.impuestos)

class Gerente(Empleado):
    '''
    Crea una clase "Gerente" que extienda de la clase "Empleado" y que tenga como propiedad adicional "departamento". 
    El método "calcular_salario_neto" de esta clase debe devolver el salario neto del gerente, restando impuestos, otros descuentos 
    y un bono adicional por ser gerente.
    '''
    bono = 0.1
    def __init__(self, nombre, apellido, sueldo, departamento):
        super().__init__(nombre, apellido, sueldo)
        self.departamento = departamento
    
    def calcular_salario_neto(self):
        return super().calcular_salario_neto() + self.sueldo*self.bono

class Programador(Empleado):
    '''
    Crea una clase "Programador" que extienda de la clase "Empleado" y que tenga como propiedad adicional "lenguaje". 
    El método "calcular_salario_neto" de esta clase debe devolver el salario neto del programador, restando impuestos, 
    otros descuentos y un bono adicional por ser experto en un lenguaje en particular.
    '''
    bono = 0.07
    def __init__(self, nombre, apellido, sueldo, lenguaje):
        super().__init__(nombre, apellido, sueldo)
        self.lenguaje = lenguaje
    
    def calcular_salario_neto(self):
        return super().calcular_salario_neto()+self.sueldo*self.bono
        