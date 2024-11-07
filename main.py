import random
from utils import mover_todas_las_personas, persona_recoge_moneda, cuantas_monedas_tiene_persona, riqueza_total, combate
from informe import grafico_evolucion_riqueza
from clases import Persona, Espacio, Moneda

''' Ejemplo de uso, voy a crear 4 personas y tres espacios, estas personas se presentarán y aparecerán en un lugar aleatorio
    con una moneda cada uno, irán moviendose aleatoriamente por los espacios se irá informando en todo momento donde están
    hasta encontrarse en algun lugar donde tienen un combate a muerte donde pierden sus monedas, inicialmente hay una moneda
    en cada espacio y en uno hay dos, el primero que llegue se las queda'''

# Creación de los espacios
espacios = {
    "Castillo": Espacio("Castillo"),
    "Jardín": Espacio("Jardín"),
}

espacio_coords = {
    "Castillo": [(1, 1), (2, 2), (3, 3)],
    "Jardín": [(4, 4), (5, 5), (6, 6)]
}

# Añadir monedas a los espacios (2 en el castillo, 1 en los demás)
espacios["Castillo"].agregar_moneda(Moneda(1, 1))
espacios["Castillo"].agregar_moneda(Moneda(1, 1))
espacios["Jardín"].agregar_moneda(Moneda(4, 4))

# Creación de personas
nombres = ["Ana", "Luis", "Carlos", "Beatriz"]
personas = []
for i, nombre in enumerate(nombres):
    año_nacimiento = random.randint(1970, 2005)
    # Asignar coordenadas iniciales según el espacio
    espacio_aleatorio = random.choice(list(espacios.values()))
    x, y = random.choice(espacio_coords["Castillo"]) 
    persona = Persona(nombre, año_nacimiento, x, y)
    personas.append(persona)
    espacio_aleatorio.agregar_persona(persona)
    persona.presentar()

# Variables para la evolución de la riqueza
riqueza_por_turno = []
turno = 0

# Bucle de simulación de movimiento y combate
while len(personas) > 1:
    print(f"\n--- Turno {turno + 1} ---")
    print(f"Personas activas en este turno: {[persona.nombre for persona in personas]}")

    # Mover personas dentro de los espacios
    for persona in personas:
        espacio_actual = next(esp for esp in espacios.values() if persona in esp.personas)
        nuevo_espacio= random.choice(["Castillo", "Jardín"])
        nueva_posicion = random.choice(espacio_coords[nuevo_espacio])  # Posición aleatoria
        persona.mover(nueva_posicion[0], nueva_posicion[1])
        persona_recoge_moneda(persona, espacio_actual)
    
    # Imprimir la ubicación de cada persona
    for persona in personas:
        print(f"{persona.nombre} está en ({persona.x}, {persona.y})")

    # Calcular e imprimir las distancias entre personas
    for i in range(len(personas)):
        for j in range(i + 1, len(personas)):
            distancia = personas[i].distancia_a(personas[j])
            print(f"La distancia entre {personas[i].nombre} y {personas[j].nombre} es {distancia:.2f}")

    # Combates entre personas en la misma posición
    eliminados = []  # Lista para guardar a las personas que serán eliminadas

    for i in range(len(personas)):
        for j in range(i + 1, len(personas)):
            if personas[i].en_misma_posicion(personas[j]):
                ganador, perdedor = combate(personas[i], personas[j])  # Ahora debería funcionar correctamente
                eliminados.append(perdedor)  # Solo añadir el perdedor

    # Procesar eliminaciones
    for persona in eliminados:
        if persona in personas:
            personas.remove(persona)
            espacio_actual = next(esp for esp in espacios.values() if persona in esp.personas)
            espacio_actual.personas.remove(persona)

    # Verificar si ya no quedan personas
    if len(personas) == 0:
        print("No quedan personas para continuar el juego.")
        break

    # Aquí se calcula la riqueza total de las personas restantes
    riqueza_total_turno = sum(persona.monedas for persona in personas)
    riqueza_por_turno.append(riqueza_total_turno)
    print(f"Riqueza total después del turno {turno + 1}: {riqueza_total_turno}")
    turno += 1


# Anunciar la persona ganadora
if len(personas) == 1:
    print(f"\n¡{personas[0].nombre} es la última persona en pie y ha ganado el juego con {personas[0].monedas} monedas!")
else:
    print("\nNo ha habido un ganador.")

# Generar gráfico de la evolución de la riqueza
turnos = list(range(1, turno + 1))
grafico_evolucion_riqueza(turnos, riqueza_por_turno)