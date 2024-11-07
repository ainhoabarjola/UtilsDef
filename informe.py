import matplotlib.pyplot as plt

def grafico_evolucion_riqueza(turnos, riqueza_por_turno):
    plt.plot(turnos, riqueza_por_turno, marker='o')
    plt.xlabel("Turno")
    plt.ylabel("Riqueza Total")
    plt.title("Evolución de la Riqueza Total por Turno")
    plt.grid(True)
    plt.show() 

def estadisticas_por_genero(personas):
    genero_riqueza = {"M": 0, "F": 0}
    for persona in personas:
        if hasattr(persona, "genero"):
            genero_riqueza[persona.genero] += persona.monedas
    return genero_riqueza

def estadisticas_por_edad(personas):
    edad_riqueza = {}
    for persona in personas:
        edad = 2024 - persona.año_nacimiento
        edad_riqueza[edad] = edad_riqueza.get(edad, 0) + persona.monedas
    return edad_riqueza


