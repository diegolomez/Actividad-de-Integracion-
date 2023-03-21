class Persona:
    def __init__(self, nombre='', edad=0, dni=''):
        self.__nombre = nombre
        self.__edad = edad
        self.__dni = dni

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_edad(self, edad):
        if edad >= 0:
            self.__edad = edad
        else:
            print('La edad no puede ser negativa.')

    def set_dni(self, dni):
        self.__dni = dni

    def get_nombre(self):
        return self.__nombre

    def get_edad(self):
        return self.__edad

    def get_dni(self):
        return self.__dni

    def mostrar(self):
        print('Nombre:', self.__nombre)
        print('Edad:', self.__edad)
        print('DNI:', self.__dni)

    def es_mayor_de_edad(self):
        return self.__edad >= 18

class Cuenta:
    def __init__(self, titular=None, cantidad=0.0):
        self.__titular = titular
        self.__cantidad = cantidad

    def set_titular(self, titular):
        self.__titular = titular

    def get_titular(self):
        return self.__titular

    def get_cantidad(self):
        return self.__cantidad

    def mostrar(self):
        print('Titular:', self.__titular.get_nombre())
        print('Cantidad:', self.__cantidad)

    def ingresar(self, cantidad):
        if cantidad > 0:
            self.__cantidad += cantidad

    def retirar(self, cantidad):
        self.__cantidad -= cantidad

class CuentaJoven(Cuenta):
    def __init__(self, titular=None, cantidad=0.0, bonificacion=0.0):
        super().__init__(titular, cantidad)
        self.__bonificacion = bonificacion

    def set_bonificacion(self, bonificacion):
        self.__bonificacion = bonificacion

    def get_bonificacion(self):
        return self.__bonificacion

    def es_titular_valido(self):
        return self.get_titular().es_mayor_de_edad() and self.get_titular().get_edad() < 25

    def retirar(self, cantidad):
        if self.es_titular_valido():
            super().retirar(cantidad)

    def mostrar(self):
        print('Cuenta Joven')
        super().mostrar()
        print('Bonificación:', self.__bonificacion)


    

        

        