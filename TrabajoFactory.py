from Trabajo import Trabajo

class TrabajoFactory:
    @staticmethod
    def crear_trabajo(descripcion, categoria, sueldoXHora, cantHoras):
        # Validaciones centralizadas aquí
        if sueldoXHora < 1000:
            sueldoXHora = 1000
        if cantHoras < 4:
            cantHoras = 4
        elif cantHoras > 8:
            cantHoras = 8

        return Trabajo(descripcion, categoria, sueldoXHora, cantHoras)
