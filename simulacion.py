import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import Slider, Button, RadioButtons

class Cuerpo_celeste:
  '''la clase cuerpo celeste tiene las variables velocidad en los ejes x r y al igual que la posicion
  estos son recalculados mas tarde con las funciones de actualizar aceleracion, velocidad, posicion.
  también como son cuerpos celestes se toma la masa del objeto'''

  def __init__(self, masa, velocidad_x, velocidad_y, posicion_x, posicion_y):
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

  # aca calculamos la posicon del objeto con ecuaciones de cinematica
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

  G = -1
  x_relativo = -objeto_2.posicion_x + objeto_1.posicion_x # aqui calculamos las posiciones a traves de relatividad galileana
  y_relativo = -objeto_2.posicion_y + objeto_1.posicion_y

  d = ((x_relativo**2) + (y_relativo**2))**(1/2)
  if d <= 0.7:
    # aca para simular que el satelite "choca" con la tierra diremos que cuando la posicion del satelite sea menor al radio de esta su velocidad y aceleracion seran 0
    objeto_1.aceleracion_x = 0 
    objeto_1.aceleracion_y = 0
    objeto_1.velocidad_x = 0
    objeto_1.velocidad_y = 0
  else:
    # para toda posicion mayor al radio del satelite la aceleracion del satelite se calcula con las ecuaciones de newton en sus respectivos ejes cartesianos
    objeto_1.aceleracion_x += G*objeto_2.masa/d**3*x_relativo
    objeto_1.aceleracion_y += G*objeto_2.masa/d**3*y_relativo

# en esta parte tomamos los valores reales de la luna, el sol y la tierra (los valores del satelites son valores estimados por nosotros)

planeta = Cuerpo_celeste(100000,0,0,0.01,0.01)#Cuerpo_celeste(6*(10**24), 0, 0, 0, 0)#
luna = Cuerpo_celeste(100,0,0,100,0)#Cuerpo_celeste(7*(10**22), 0, 0, 275000000, 275000000)#
satelite = Cuerpo_celeste(0.1,50,10.1,0,2)#Cuerpo_celeste(200, 100, -1150, 2000,2000)#
Sol = Cuerpo_celeste(1e7,0,0,-1e4,0)
Delta_T = 0.0004 #86400
trayectoria_x = [] # se crea una lista para agregar las posiciones enesimas del satelite para el eje x cartesiano
trayectoria_y = [] # se crea una lista para agregar las posiciones enesimas del satelite para el eje y cartesiano
trayectoria_x.append(satelite.posicion_x) # aqui se agregan los primeros valores del satelite a la lista anterior (eje x)
trayectoria_y.append(satelite.posicion_y) # aqui se agregan los primeros valores del satelite a la lista anterior (eje y)

# en esta parte usaremos un integrador orbital más especificamente leapfrog con la finalidad de reducir errores en los calculos la  orbita

for k in range(99999): # definimos un rango largo de iteraciones para asi asegurarnos de completar al menos una orbita 
    if k < 5: 
      # para las primeras cinco iteraciones queremos que nuestro satelite mantenga una velocidad constante por ende queremos actualizar la velocidad
      actualizacion_posicion(satelite, Delta_T) # esta funcion nos entrega las posiciones en los ejes cartesianos
      trayectoria_x.append(satelite.posicion_x) # agregamos las siguientes cinco iteraciones de la posicion con velocidad constante (eje x)
      trayectoria_y.append(satelite.posicion_y) # agregamos las siguientes cinco iteraciones de la posicion con velocidad constante (eje y)
    else:
      actualizacion_aceleracion(satelite, planeta) # utilizamos la funcion anterior para calcular la aceleracion del satelite
      actualizacion_velocidad(satelite, Delta_T/2) # utilizamos la funcion anterior para calcular la velocidad del satelite para cada iteracion
      actualizacion_posicion(satelite, Delta_T) 
      trayectoria_x.append(satelite.posicion_x) # agregamos las iteraciones restantes de la posicion 
      trayectoria_y.append(satelite.posicion_y) 
      satelite.aceleracion_x = 0 # para evitar la sobreescritura de la aceleracion al final de cada iteracion la aceleracion es igual a cero
      satelite.aceleracion_y = 0 

m_velocidad = np.sqrt(satelite.velocidad_x0**2 + satelite.velocidad_y0**2) # definimos una velocidad incial para el satélite
angulo = np.arctan(satelite.velocidad_y0/satelite.velocidad_x0)# definimos el ángulo del lanzamiento del satélite


fig, ax = plt.subplots(figsize=(15, 8)) # creamos una figura y un subconjunto de graficos y ajustamos el tamaño de la figura
plt.subplots_adjust(left=0.3, right=0.95, bottom=0.2, top = 0.9) # ajustamos el espacio alrededor de los subgraficos

# aqui asignamos los colores de los graficos
fig.set_facecolor('whitesmoke') 
ax.set_facecolor('#24113A')


ax_slider = plt.axes([0.25, 0.03, 0.60, 0.04])  # Posición del slider
# slider_velocidad tiene las componentes: nombre (velocidad), valor minimo, valor maximo, valor inicial del slider
slider_velocidad = Slider(ax_slider, 'Velocidad', valmax=m_velocidad*10, valmin=m_velocidad/10, valinit=m_velocidad)


ax_slider2 = plt.axes([0.25, 0.01, 0.60, 0.02])  # Posición del slider
slider_angulo = Slider(ax_slider2, 'Angulo', valmax=np.pi, valmin=0, valinit=angulo) # es lo mismo que el slider de velocidad pero con angulos
ax_slider2.invert_xaxis()
#slider_angulo.valmin, slider_angulo.valmax = slider_angulo.valmax, slider_angulo.valmin

ax_inicio = plt.axes([0.1, 0.07, 0.1, 0.04]) # posición del botón de inicio
ax_pause = plt.axes([0.1, 0.02, 0.1, 0.03])  # Posición del botón de pausa
ax_reiniciar = plt.axes([0.88, 0.01, 0.1, 0.03])  # Posición del botón de reiniciar

# asignamos botones a inicio, pausa y reiniciar
btn_inicio = Button(ax_inicio, 'Iniciar') 
btn_pause = Button(ax_pause, 'Pausar')
btn_reiniciar = Button(ax_reiniciar, 'Reiniciar')


# Configuración inicial
set_variable = 'Tierra Satelite'
limitex,limitey = (-10,10),(-10,10) # establecemos los limites de las animaciones
ax_options = plt.axes([0.03, 0.6, 0.23, 0.28])

# Crear radio buttons
options = ['Tierra Satelite', 'Tierra Luna', 'Tierra Sol']
radio_buttons = RadioButtons(ax_options, options, active=0)


# Función que se ejecutará al seleccionar una opción
def on_radiobuttons_clicked(label):
    global set_variable, limitex, limitey # utilizaremos los valores 
    set_variable = label
    limitex,limitey = (-10,10),(-10,10) # establecemos los limites de las animaciones dependoiendo del set_variable
    reiniciar_animacion(0) # simplemente utilizamos la funcion

def iniciar_animacion(event):
    '''esta funcion sirve solamente para iniciar la funcion con los valores actuales de los objetos e iteraciones
    
    funciona haciendo click en el boton "iniciar"'''

    ani.event_source.start() # comenzamos la animacion

def pausar_animacion(event):
    '''un funcion para parar la animacion
    
    funciona haciendo click en el boton "pausar" '''

    ani.event_source.stop() # paramos la animacion

def reiniciar_animacion(event):
    ''' esta funcion tiene como objetivo reiniciar, todos los valores anteriores a un punto incial
    
    funciona solamente haciendo click en el boton "reiniciar" '''
    global trayectoria_x, trayectoria_y, limitex, limitey # aca el boton reiniciar, hace que todos los valores vuelvan a los valores iniciales
    velocidad_x = slider_velocidad.val*np.cos(slider_angulo.val)
    velocidad_y = slider_velocidad.val*np.sin(slider_angulo.val)
    satelite = Cuerpo_celeste(0.1,velocidad_x,velocidad_y,0,2)
    trayectoria_x = []
    trayectoria_y = []
    trayectoria_x.append(satelite.posicion_x)
    trayectoria_y.append(satelite.posicion_y)

    for k in range(99999): # este siclo es el mismo que el siclo anterior

        if k < 5:
          actualizacion_posicion(satelite, Delta_T)
          trayectoria_x.append(satelite.posicion_x)
          trayectoria_y.append(satelite.posicion_y)

        else:

          actualizacion_aceleracion(satelite, planeta)

          if set_variable == 'Tierra Luna':
            actualizacion_aceleracion(satelite, luna)
            limitex,limitey = (-100,100),(-100,100)

          elif set_variable == 'Tierra Sol':
            actualizacion_aceleracion(satelite, Sol)
            limitex,limitey = (-2e4,1e4),(-1e4,1e4)

          actualizacion_velocidad(satelite, Delta_T/2)
          actualizacion_posicion(satelite, Delta_T)
          trayectoria_x.append(satelite.posicion_x)
          trayectoria_y.append(satelite.posicion_y)
          satelite.aceleracion_x = 0
          satelite.aceleracion_y = 0

    ani.event_source.start()
    ani.frame_seq = ani.new_frame_seq()

# Conectar la función al evento de selección
radio_buttons.on_clicked(on_radiobuttons_clicked)
btn_inicio.on_clicked(iniciar_animacion)
btn_pause.on_clicked(pausar_animacion)
btn_reiniciar.on_clicked(reiniciar_animacion)

vel = int(input('ingrese la velocidad de la animacion: '))


def actualizar(i):
    '''actualizar es la funcion base para la animacion, ya que esta se encarga de actualizar la posicion del satelite, en distintos 
    sistemas de cuerpos, ya sea tierra-luna, tierra-satelite, tierra-sol
    
    la funcion nos entrega el punto del satelite (dot) y la trayectoria del satelite (line)'''
    if i == 0:
      ani.event_source.stop()  # Pausar animación después del primer frame

    ax.clear()  # Limpiar el eje en cada frame
    dot = ax.plot(trayectoria_x[i*vel], trayectoria_y[i*vel], '.')  # Agregar nuevo punto
    line = ax.plot(trayectoria_x[:(i*vel)], trayectoria_y[:(i*vel)], '--')
    ax.plot(planeta.posicion_x, planeta.posicion_y, "go")  # Mantener el punto del planeta
    if set_variable == 'Tierra Luna':
      ax.plot(luna.posicion_x, luna.posicion_y, "o",c='grey')
    if set_variable == 'Tierra Sol':
      ax.plot(Sol.posicion_x, Sol.posicion_y, "o",c=('#FFCE2F'),markersize=200)
    ax.set_xlim(limitex)
    ax.set_ylim(limitey)


    ax.grid(alpha=0.1,linestyle='-.')


    return [dot,line]#trayectoria_line,


ani = FuncAnimation(fig, actualizar, frames=int(len(trayectoria_x)/vel), interval=1, blit=False)#init_func=inicializar

plt.show()
