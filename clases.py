import math
class Persona:
    def __init__(self, nombre, año_nacimiento, x, y):
        self.nombre = nombre
        self.año_nacimiento = año_nacimiento
        self.x = x
        self.y = y
        self.monedas = 1  #Monedas que tiene

    def mover(self, nuevo_x, nuevo_y): #Para mover a la persona
        self.x = nuevo_x
        self.y = nuevo_y

    def distancia_a(self, otra_persona): #Distancia entre dos personas
        return math.sqrt((self.x - otra_persona.x) ** 2 + (self.y - otra_persona.y) ** 2)

    def en_misma_posicion(self, otra_persona):
        return self.x == otra_persona.x and self.y == otra_persona.y

    def presentar(self): #Presenta la información de la persona.
        print(f"Hola, soy {self.nombre}, nací en el año {self.año_nacimiento}. Estoy en ({self.x}, {self.y}) y tengo {self.monedas} monedas.")


class Espacio:
    def __init__(self, nombre):
        self.nombre = nombre
        self.personas = []
        self.monedas = []

    def agregar_persona(self, persona):
        self.personas.append(persona)

    def contar_personas(self):
        return len(self.personas)

    def agregar_moneda(self, moneda): #Añade una moneda a un espacio
        self.monedas.append(moneda)

class Moneda:
    def __init__(self, x, y): #Posición de la moneda
        self.x = x
        self.y = y
