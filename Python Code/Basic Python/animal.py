# Author: Luis Felipe Castro Sánchez
# Creation Date: 12/11/18
# GitHub User: luisfelipe7
# Version: 1.0.0
# Country: Costa Rica


class Animal(object):

    def __init__(self, *args):
        self.nombre = args[0]
        self.edad = args[1]
        self.color = args[2]

    def aumentaEdad(self):
        self.edad += 1

    def muestraDatos(self):
        datos = 'Nombre: '+self.nombre + ' Edad: ' + \
            str(self.edad) + ' Color: '+self.color
        return datos
