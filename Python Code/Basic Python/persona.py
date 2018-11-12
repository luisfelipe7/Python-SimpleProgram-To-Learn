class Persona(object):

    #     def __init__(self):  # Constructor sin parametros
    #        self.nombre = "Nombre"
    #        self.edad = 0
    #        self.ciudad = "Heredia"

    def __init__(self, *args):  # Constructor con parametros
        self.nombre = args[0]
        self.edad = args[1]
        self.ciudad = args[2]

    def presentacion(self):
        return (" Hola soy {}, tengo {} anios y vivo en {}.".format(
            self.nombre, self.edad, self.ciudad))

    def implicit(self):
        return "This function is for everyone, included my sons"

# Con Parametros
# personaDefault = Persona("Felipe", 20, "Heredia")
# personaDefault.presentacion()

# Sin Parametros
# personaDefault = Persona(")
# personaDefault.presentacion()
