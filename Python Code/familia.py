import animal


class Familia(object):

    def __init__(self, *args):
        self.animal1 = animal.Animal(*args)

    def aumentaEdad(self):
        self.animal1.aumentaEdad()

    def muestraDatos(self):
        return self.animal1.muestraDatos()


# familia1 = Familia('Mono', 2, 'Negro')
# familia1.aumentaEdad()
# print(familia1.muestraDatos())
