import persona


class Empleado(persona.Persona):

    def __init__(self, *args):
        super().__init__(*args)
        self.sueldo = args[3]

    def presentacion(self):
        print(super().presentacion(), "Mi sueldo es {}".format(self.sueldo))


# personaEmpleado = Empleado("Felipe", 20, "Heredia", "50000")
# personaEmpleado.presentacion()
