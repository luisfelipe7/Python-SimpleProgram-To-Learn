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

# animal1 = Animal('Mono', 2, 'Negro')
# print("Datos del animal1", animal1.muestraDatos())
# animal1.aumentaEdad()
# print("Datos del animal1", animal1.muestraDatos())
