# Simulacion_satelite
Software de simulación para una trayectoria de un satélite alrededor del planeta, considerando la Luna o el Sol.

### Problemática a solucionar
Si un cuerpo desea salir de la atracción gravitacional de la tierra desde su superficie, necesita ir a determinada velocidad, llamada velocidad de escape, esto dependiendo de la masa del planeta (11 km por segundo en el caso del Planeta Tierra ). Esta simulación sirve para ver a qué velocidades es factible que un satélite escape de la Tierra y con qué ángulo de lanzamiento desde la superficie de este.
También se puede considerar el caso en que el satélite colisione con la luna, entonces podemos ver (dependiendo de la posición inicial de la luna ), si es que nuestro satélite puede o no colisionar con la luna.

**¿Sirve la aproximación newtoniana?**

Como sabemos las ecuaciones de newton son buenas siempre y cuando se utilicen en modelos de dos cuerpos, en cambio cuando se agrega un tercero, esta aproximación comienza a fallar. Para solucionar esto, utilizamos un integrador orbital conocido como leapfrog, el cual es bueno específicamente para escalas de tiempo más grandes.
La computación agiliza con el problema, permitiendo ver el comportamiento a través de varias iteraciones aplicando el integrador leapfrog.

### Variables requeridas por el código
Como se van a ocupar las ecuación de leapfrog, y gravitacional, se necesita de :

  >* Velocidad inicial
  >* Ángulo de lanzamiento
  >* Masa de los cuerpos
  >* Posición de los cuerpos

### Output

  >* Gráfico con los cuerpos.

2 Barras : 

  >* La rapidez inicial.
  >* El ángulo de disparo.

3 Opciones : 

  >* El satélite orbitando la Tierra
  >* El satélite orbitando la Tierra, considerando la Luna
  >* El satélite orbitando la Tierra, considerando la Luna y el Sol

3 Botones : 

  >* Iniciar: Inicia la animación
  >* Pausar: Pausa la animación
  >* Aplicar/Reiniciar: Aplica los cambios de la velocidad y angulo de las barras / reinicia la animación.


### Versiones de las librerías

  >* numpy = 1.26.2
  >* matplotlib = 3.5.1
