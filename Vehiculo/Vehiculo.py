class Vehiculo:
   '''
   Define una clase "Vehiculo" que tenga como propiedades(atributos) "marca", "modelo" y "año". 
   También debe tener un método "obtener_info" que muestre la información del vehículo.
   '''
   def __init__(self,marca, modelo, año):
       self.marca = marca
       self.modelo = modelo
       self.año = año
    
   def obtener_info(self):
       return f'El vehiculo es un {self.marca}\nModelo: ${self.modelo}\nAño: ${self.año}'
   
class AutoMovil(Vehiculo):
    '''
    Crea una clase "Automovil" que extienda de la clase "Vehiculo" y que tenga como propiedad adicional "numero_puertas". 
    El método "obtener_info" de esta clase debe mostrar la información del automóvil, incluyendo el número de puertas.
    '''
    def __init__(self, marca, modelo, año, numero_puertas):
        super().__init__(marca, modelo, año)
        self.numero_puertas = numero_puertas
    
    def obtener_info(self):
        return f'${super().obtener_info()}\nNumero de puertas:${self.numero_puertas}'

class Camioneta(AutoMovil):
    '''
    Crea una clase "Camioneta" que extienda de la clase "Vehiculo" y que tenga como propiedad adicional "capacidad_carga". 
    El método "obtener_info" de esta clase debe mostrar la información de la camioneta, incluyendo la capacidad de carga.
    '''
    def __init__(self, marca, modelo, año, numero_puertas, capacidad_carga):
        super().__init__(marca, modelo, año, numero_puertas)
        self.capacidad_carga = capacidad_carga
    
    def obtener_info(self):
        return f'${super().obtener_info()}\nCapacidad de carga:${self.capacidad_carga}'