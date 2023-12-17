import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import Slider, Button, RadioButtons
import matplotlib.patches as patches


class Cuerpo_celeste:
  '''la clase cuerpo celeste tiene las variables: nombre, velocidad en los ejes x r y al igual que la posicion
  estos son recalculados mas tarde con las funciones de actualizar aceleracion, velocidad, posicion.
  también como son cuerpos celestes se toma la masa del objeto'''
  def __init__(self, nombre, masa, velocidad_x, velocidad_y, posicion_x, posicion_y):
    self.nombre = nombre
    self.posicion_x = posicion_x
    self.posicion_y = posicion_y
    self.velocidad_x0 = velocidad_x
    self.velocidad_y0 = velocidad_y
    self.velocidad_x = velocidad_x
    self.velocidad_y = velocidad_y
    self.aceleracion_x = 0
    self.aceleracion_y = 0
    self.masa = masa

def actualizacion_posicion(objeto, delta_t):
  '''la función altualizacion_posicion toma como variables : objeto y delta_t la variable objeto corresponde
  a la clase: cuerpo_celeste con sus respectivos valores, y delta_t es una variable definida por nosotros
  luego actualica la posicion con una ecuacion que toma la posicion enesima del objeto y lo multiplica por delta_t

  lo que nos entrega esta funcion son las posiciones enesimas del cuerpo a observar (ejes x e y)'''

  # aca calculamos la posicion del objeto con ecuaciones de cinematica
  objeto.posicion_x += objeto.velocidad_x*delta_t
  objeto.posicion_y += objeto.velocidad_y*delta_t

def actualizacion_velocidad(objeto, delta_t):
  '''la función altualizacion_velocidad toma como variables : objeto y delta_t la variable objeto corresponde
  a la clase: cuerpo_celeste con sus respectivos valores, y delta_t es una variable definida por nosotros
  al igual que la funcion anterior, en este caso toma la aceleracon enesima del objeto y lo multiplica por delta_t

  lo que nos entrega esta funcion son las velocidades en los ejer cartesianos'''

  # aca calculamos la velocidad del objeto con ecuaciones de cinematica
  objeto.velocidad_x += objeto.aceleracion_x*delta_t
  objeto.velocidad_y += objeto.aceleracion_y*delta_t

def actualizacion_aceleracion(objeto_1, objeto_2):
  '''la funcion actualizacion_ aceleracion considera la constante de gravitacion de newton para luego calcular una posicion
  relativa (a través de relatividad galileana) y así posteriormente calcular (a través de ecuaciones de newton) la aceleración
  en los ejes cartesianos.

  lo que nos entrega esta funcion son las aceleraciones enesimas del objeto'''

  global f


  # cálculo de las posiciones con relatividad galileana
  x_relativo = -objeto_2.posicion_x + objeto_1.posicion_x
  y_relativo = -objeto_2.posicion_y + objeto_1.posicion_y

  # cálculo de la distancia tierra-saltelite
  d = ((x_relativo**2) + (y_relativo**2))**(1/2)

  # defininimos los radios de los cuerpos selestes, por lo tanto en caso de ser menor al radio de uno de estos el satelite "choca" y su velocidad será 0
  if objeto_2.nombre == 'Tierra':
    if d <= 6400e3:
      objeto_1.aceleracion_x = 0
      objeto_1.aceleracion_y = 0
      objeto_1.velocidad_x = 0
      objeto_1.velocidad_y = 0
      f.append(k) # f es una lista que va a ir tomando todos los indices del ciclo.
    else:
      objeto_1.aceleracion_x += G*objeto_2.masa/d**3*x_relativo
      objeto_1.aceleracion_y += G*objeto_2.masa/d**3*y_relativo
  if objeto_2.nombre == 'Luna':
      if d <= 1704e3:
        objeto_1.aceleracion_x = 0
        objeto_1.aceleracion_y = 0
        objeto_1.velocidad_x = 0
        objeto_1.velocidad_y = 0
        f.append(k)
      else:
        objeto_1.aceleracion_x += G*objeto_2.masa/d**3*x_relativo
        objeto_1.aceleracion_y += G*objeto_2.masa/d**3*y_relativo
  if objeto_2.nombre == 'Sol':
      if d <= 0.69e9:
        objeto_1.aceleracion_x = 0
        objeto_1.aceleracion_y = 0
        objeto_1.velocidad_x = 0
        objeto_1.velocidad_y = 0
        f.append(k)
      else:
        objeto_1.aceleracion_x += G*objeto_2.masa/d**3*x_relativo
        objeto_1.aceleracion_y += G*objeto_2.masa/d**3*y_relativo

# Función que se ejecutará al seleccionar una opción
def on_radiobuttons_clicked(label):
    global set_variable, limitex, limitey # utilizaremos los valores
    set_variable = label
    limitex,limitey = (-6400e4,6400e4),(-6400e4,6400e4) # establecemos los limites de las animaciones dependoiendo del set_variable
    reiniciar_animacion(0) # simplemente utilizamos la funcion

def iniciar_animacion(event):
    '''esta funcion sirve solamente para iniciar la funcion con los valores actuales de los objetos e iteraciones

    funciona haciendo click en el boton "iniciar"'''

    ani.event_source.start() # comenzar la animacion

def pausar_animacion(event):
    '''un funcion para parar la animacion

    funciona haciendo click en el boton "pausar" '''

    ani.event_source.stop() # paramos la animacion

def reiniciar_animacion(event):
    ''' esta funcion tiene como objetivo reiniciar, todos los valores anteriores a un punto incial

    funciona solamente haciendo click en el boton "reiniciar" '''

    global trayectoria_x, trayectoria_y, limitex, limitey, f,k # aca el boton reiniciar, hace que todos los valores vuelvan a los valores iniciales
    velocidad_x = slider_velocidad.val*np.cos(slider_angulo.val)
    velocidad_y = slider_velocidad.val*np.sin(slider_angulo.val)
    satelite = Cuerpo_celeste('Satelite',8e3,velocidad_x,velocidad_y,0,1.5*6400e3)
    trayectoria_x = []
    trayectoria_y = []
    trayectoria_x.append(satelite.posicion_x)
    trayectoria_y.append(satelite.posicion_y)
    f=[]

    for k in range(99999): # este siclo es el mismo que el siclo anterior

        if k < 100:
          actualizacion_posicion(satelite, Delta_T)
          trayectoria_x.append(satelite.posicion_x)
          trayectoria_y.append(satelite.posicion_y)

        else:

          actualizacion_aceleracion(satelite, planeta)


          if set_variable == 'Tierra Luna':
            actualizacion_aceleracion(satelite, luna)
            limitex,limitey = ((-1.5)*384e6,(1.5)*384e6),(-384e6,384e6)

          elif set_variable == 'Tierra Sol':
            actualizacion_aceleracion(satelite, Sol)
            limitex,limitey = ((-1.2)*150e9,(0.5)*150e9),(-150e9,150e9)

          actualizacion_velocidad(satelite, Delta_T/2)
          actualizacion_posicion(satelite, Delta_T)
          trayectoria_x.append(satelite.posicion_x)
          trayectoria_y.append(satelite.posicion_y)

          satelite.aceleracion_x = 0
          satelite.aceleracion_y = 0


    ani.event_source.start()
    ani.frame_seq = ani.new_frame_seq()

def actualizar(i):
    '''actualizar es la funcion base para la animacion, ya que esta se encarga de actualizar la posicion del satelite, en distintos
    sistemas de cuerpos, ya sea tierra-luna, tierra-satelite, tierra-sol

    la funcion nos entrega el punto del satelite (dot) y la trayectoria del satelite (line)'''

    if i == 0:
      ani.event_source.stop()  # Pausar animación después del primer frame

    if len(f) > 0:

      if f[0] < i*vel:
        ani.event_source.stop()


    ax.clear()  # Limpiar el eje en cada frame
    dot = ax.plot(trayectoria_x[i*vel], trayectoria_y[i*vel], '.')  # Agregar nuevo punto
    line = ax.plot(trayectoria_x[:(i*vel)], trayectoria_y[:(i*vel)], '--') # marca la trayectoria del satelite

    planet_circle = patches.Circle((planeta.posicion_x, planeta.posicion_y), radius=6400e3, edgecolor='g', facecolor='g') # funcion para hacer un circulo con el radio del planeta
    ax.add_patch(planet_circle) # añadir el circulo a el grafico

    # Agregar nuevo círculo para representar la luna si es necesario
    if set_variable == 'Tierra Luna':
        luna_circle = patches.Circle((luna.posicion_x, luna.posicion_y), radius=1704e3, edgecolor='grey', facecolor='grey')
        ax.add_patch(luna_circle)

    # Agregar nuevo círculo para representar el Sol si es necesario
    if set_variable == 'Tierra Sol':
        sol_circle = patches.Circle((Sol.posicion_x, Sol.posicion_y), radius=6.96e8, edgecolor='#FFCE2F', facecolor='#FFCE2F')
        ax.add_patch(sol_circle)

    #definir los limites de las
    ax.set_xlim(limitex)
    ax.set_ylim(limitey)

    # le colocamos los respectivos nombres de los ejes y titulo a los graficos
    plt.title(f'Tiempo recorrido: {i*vel*Delta_T} segundos')
    ax.set_title(f'Simulación órbita: {set_variable}',fontsize=25)
    ax.set_xlabel('distancia [m]',fontsize=10)
    ax.set_ylabel('distancia [m]',fontsize=10)

    ax.grid(alpha=0.1,linestyle='-.')


    return [dot,line]

#%%

# en esta parte tomaremos los valores reales de los cuerpos celestes a estudiar (los valores del satelite son valores estimados por nosotros)

planeta = Cuerpo_celeste('Tierra',6e24,0,0,0.01,0.01)
luna = Cuerpo_celeste('Luna',7e22,0,0,384e6,0)
satelite = Cuerpo_celeste('Satelite',8e3,5451,0.01,0,1.5*6400e3)
Sol = Cuerpo_celeste('Sol',2e30,0,0,-150e9,0)
Delta_T = 10
G = -6.67e-11 # constante de gravitacion universal
trayectoria_x = [] # se crea una lista para agregar las posiciones enesimas del satelite para el eje x cartesiano
trayectoria_y = [] # se crea una lista para agregar las posiciones enesimas del satelite para el eje x cartesiano


# agregamos los primeros valores de la posicion del satelite en sus respectivos ejes (x e y)
trayectoria_x.append(satelite.posicion_x)
trayectoria_y.append(satelite.posicion_y)

f = [] # se crea una lista que va a tomar todos los valores de k el cual sera los valores de iteraciones

# aqui utilizaremos leapfrog con la finalidad de reducir errores en los calculos de la orvita

for k in range(99999): # definimos un rango largo de iteraciones para así, asegurarnos de completar al menos una orbita
    if k < 100:
      # para las primeras cinco iteraciones queremos qie niestro satelite mantenga una velocidad constante por ende no queremos actualizar la velocidad
      actualizacion_posicion(satelite, Delta_T) # esta funcion nos entrega las posiciones en los ejes cartesianos
      trayectoria_x.append(satelite.posicion_x) # agregamos las siguientes cinco iteraciones de la posicion con velocidad constante (eje x)
      trayectoria_y.append(satelite.posicion_y) # agregamos las siguientes cinco iteraciones de la posicion con velocidad constante (eje y)
    else:
      actualizacion_aceleracion(satelite, planeta) # utilizamos la funcion anterior para calcular la aceleracion del satelite
      actualizacion_velocidad(satelite, Delta_T/2) # utilizamos la funcion anterior para calcular la velocidad del satelite para cada iteracion
      actualizacion_posicion(satelite, Delta_T)
      trayectoria_x.append(satelite.posicion_x) # agregamos las iteraciones restantes de la posicion a la lista de la trayectoria
      trayectoria_y.append(satelite.posicion_y)

      satelite.aceleracion_x = 0 # para evitar la sobreescritura de la aceleracion al final de cada iteracion la aceleracion es igual a cer
      satelite.aceleracion_y = 0


m_velocidad = np.sqrt(satelite.velocidad_x0**2 + satelite.velocidad_y0**2) # definimos una velocidad incial para el satélite
angulo = np.arctan(abs(satelite.velocidad_y0)/abs(satelite.velocidad_x0)) # definimos el ángulo del lanzamiento del satélite


fig, ax = plt.subplots(figsize=(10, 8)) # creamos una figura y un subconjunto de graficos y ajustamos el tamaño de la figura
plt.subplots_adjust(left=0.35, right=0.98, bottom=0.2, top = 0.9) # ajustamos el espacio alrededor de los subgraficos

# aqui asignamos los colores de los graficos
plt.style.use(['dark_background'])
fig.set_facecolor('black')
ax.set_facecolor('#24113A')


ax_slider = plt.axes([0.346, 0.09, 0.57, 0.06])  # Posición del slider
# slider_velocidad tiene las componentes: nombre (velocidad), valor minimo, valor maximo, valor inicial del slider
slider_velocidad = Slider(ax_slider, 'Velocidad', valmax=m_velocidad*10, valmin=m_velocidad/10, valinit=m_velocidad)


ax_slider2 = plt.axes([0.346, 0.03, 0.57, 0.06])  # Posición del slider
slider_angulo = Slider(ax_slider2, 'Angulo', valmax=np.pi, valmin=0, valinit=angulo) # es lo mismo que el slider de velocidad pero con angulos
ax_slider2.invert_xaxis() # aca se invierte el slider para facilitar


ax_inicio = plt.axes([0.03, 0.45, 0.23, 0.098]) # posicion de boton inicio
ax_pause = plt.axes([0.03, 0.3, 0.23, 0.098])  # Posición del botón de pausa
ax_reiniciar = plt.axes([0.03, 0.15, 0.23, 0.098])  # Posición del botón de reiniciar

# asignamos botones a inicio, pausa y reiniciar
btn_inicio = Button(ax_inicio, 'Iniciar',color='black')
btn_pause = Button(ax_pause, 'Pausar',color='black')
btn_reiniciar = Button(ax_reiniciar, 'Aplicar / Reiniciar',color='black')


# Configuración inicial
set_variable = 'Tierra Satelite'
limitex,limitey = (-6400e4,6400e4),(-6400e4,6400e4) # establecemos los limites de las animaciones
ax_options = plt.axes([0.03, 0.6, 0.23, 0.28])

# Crear radio buttons
options = ['Tierra Satelite', 'Tierra Luna', 'Tierra Sol']
radio_buttons = RadioButtons(ax_options, options, active=0)

# Conectar la función al evento de selección
radio_buttons.on_clicked(on_radiobuttons_clicked)
btn_inicio.on_clicked(iniciar_animacion)
btn_pause.on_clicked(pausar_animacion)
btn_reiniciar.on_clicked(reiniciar_animacion)

vel= 100

ani = FuncAnimation(fig, actualizar, frames=int(len(trayectoria_x)/vel), interval=1, blit=False)

plt.show()
