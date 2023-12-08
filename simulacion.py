import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

G = 6.67430e-11  # Constante gravitacional
m_earth = 5.972e24  # Masa de la Tierra
m_satellite = 10**-20 # Masa del satélite
m_moon = 7.342e22  # Masa de la Luna

class CuerpoCeleste:
    def __init__(self, masa, posicion, velocidad):
        self.masa = masa
        self.posicion = np.array(posicion, dtype=float)
        self.velocidad = np.array(velocidad, dtype=float)

def calcular_aceleracion(cuerpo, otros_cuerpos):
    aceleracion = np.zeros(2)
    for otro_cuerpo in otros_cuerpos:
        if cuerpo != otro_cuerpo:
            r_vector = otro_cuerpo.posicion - cuerpo.posicion
            r = np.linalg.norm(r_vector)
            fuerza_gravitatoria = G * otro_cuerpo.masa * cuerpo.masa / r**3 * r_vector
            aceleracion += fuerza_gravitatoria / cuerpo.masa
    return aceleracion

def leapfrog(cuerpos, delta_t):
    for cuerpo in cuerpos:
        cuerpo.velocidad += 0.5 * calcular_aceleracion(cuerpo, cuerpos) * delta_t
        cuerpo.posicion += cuerpo.velocidad * delta_t
        cuerpo.velocidad += 0.5 * calcular_aceleracion(cuerpo, cuerpos) * delta_t

# Condiciones iniciales
radio_tierra = 6400 #km
tierra = CuerpoCeleste(masa=m_earth, posicion=[0, 0], velocidad=[0, 0])
luna = CuerpoCeleste(masa=m_moon, posicion=[384400e3, 0], velocidad=[0, 1000])
satelite = CuerpoCeleste(masa=m_satellite, posicion=[7000e3, 0], velocidad=[0, 7500])

# Parámetros de la simulación
delta_t = 1000  # Paso de tiempo en segundos
num_pasos = 1000

# Crear la figura y el eje
fig, ax = plt.subplots()
ax.set_xlim(-5e8, 5e8)
ax.set_ylim(-5e8, 5e8)

# Crear objetos de trayectoria
trayectoria_tierra, = ax.plot([], [], 'b-', label='Tierra')
trayectoria_luna, = ax.plot([], [], 'y-', label='Luna')
trayectoria_satelite, = ax.plot([], [], 'r-', label='Satélite')
punto_tierra, = ax.plot([], [], 'bo')
punto_luna, = ax.plot([], [], 'go')
punto_satelite, = ax.plot([], [], 'ro')

# Función de inicialización de la animación
def init():
    trayectoria_tierra.set_data([], [])
    trayectoria_luna.set_data([], [])
    trayectoria_satelite.set_data([], [])
    punto_tierra.set_data([], [])
    punto_luna.set_data([], [])
    punto_satelite.set_data([], [])
    return trayectoria_tierra, trayectoria_luna, trayectoria_satelite, punto_tierra, punto_luna, punto_satelite

# Función de actualización de la animación
def update(frame):
    leapfrog([tierra, luna, satelite], delta_t)
    x_tierra, y_tierra = trayectoria_tierra.get_data()
    x_luna, y_luna = trayectoria_luna.get_data()
    x_satelite, y_satelite = trayectoria_satelite.get_data()

    x_tierra.append(tierra.posicion[0])
    y_tierra.append(tierra.posicion[1])
    x_luna.append(luna.posicion[0])
    y_luna.append(luna.posicion[1])
    x_satelite.append(satelite.posicion[0])
    y_satelite.append(satelite.posicion[1])

    trayectoria_tierra.set_data(x_tierra, y_tierra)
    trayectoria_luna.set_data(x_luna, y_luna)
    trayectoria_satelite.set_data(x_satelite, y_satelite)
    punto_tierra.set_data(tierra.posicion[0], tierra.posicion[1])
    punto_luna.set_data(luna.posicion[0], luna.posicion[1])
    punto_satelite.set_data(satelite.posicion[0], satelite.posicion[1])

    return trayectoria_tierra, trayectoria_luna, trayectoria_satelite, punto_tierra, punto_luna, punto_satelite

# Crear la animación
ani = FuncAnimation(fig, update, frames=num_pasos, init_func=init, blit=True)

# Mostrar la leyenda
ax.legend()

# Mostrar la animación
plt.show()

