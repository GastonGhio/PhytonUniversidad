from persona import persona


# poniendo persona hago que herede todas lkas cateristicas de esa clase
class cliente(persona):
    def __init__(self, nombre, apellido, dni, telefono, categoria):
        super().__init__(nombre, apellido, dni, telefono)
        self.categoria = categoria

