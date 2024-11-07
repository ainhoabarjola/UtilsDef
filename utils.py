import random

def mover_todas_las_personas(espacio, x_max, y_max): #Mueve a todas las personas a una nueva posición aleatoria dentro de un límite dado
    for persona in espacio.personas:
        nueva_x = random.randint(0, x_max)
        nueva_y = random.randint(0, y_max)
        persona.mover(nueva_x, nueva_y)

def persona_recoge_moneda(persona, espacio): #Permite que una persona recoja una moneda si están en la misma posición.
    for moneda in espacio.monedas:
        if persona.x == moneda.x and persona.y == moneda.y:
            persona.monedas += 1
            espacio.monedas.remove(moneda)  #Paara quitar la moneda del espacio
            break

def cuantas_monedas_tiene_persona(persona): #Te dice la cantidad de monedas de una persona.
    return persona.monedas

def riqueza_total(espacio): #Te dice el total de monedas de todas las personas en el espacio.
    return sum(persona.monedas for persona in espacio.personas)

def combate(persona1, persona2):  # Simula un combate entre dos personas en la misma posición, eliminando a una de ellas.
    if persona1.en_misma_posicion(persona2):
        perdedor = persona1 if random.choice([True, False]) else persona2
        ganador = persona1 if perdedor is persona2 else persona2  # Define el ganador
        perdedor.monedas = 0  # El perdedor pierde todas las monedas
        print(f"{perdedor.nombre} ha perdido el combate y pierde todas sus monedas.")
        return ganador, perdedor  # Retornar el ganador y el perdedor