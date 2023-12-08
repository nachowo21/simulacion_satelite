# simulacion_satelite
programa para simular la trayectoria de un satelite considerando un sistema tierra-luna

### problematica a solucionar
sabemos que los planetas poseen velocidad de escape, esto dependiendo la masa del planeta (para nuestro caso son 11 km por segundo), esta simulacion sirve para ver a que velocidades es factibles que un satelite salga de la estrella y con qué ángulo de lanzamiento.
por otro lado tenemos un posible caso en el cual el satelite puede colisionar con la luna, entonces podemos ver (dependiendo de la posicion inicial de la luna ), si es que nuestro satelite puede o no colisionar con la luna.

**¿sirve la aporximacion newtoniana?**

Como sabemos las ecuaciones de newton son buenas siempre y cuando se utilicen en modelos de dos cuerpos, en cambio cuando se agrega un tercero, esta aproximación comienza a fallar. Para solucionar esto, utilizamos un integrador orbital conocido como leapfrog, el cual es bueno especificamente para escalas de tiempo mas grandes.
la computacion nos soluciona este problema ya que para ver el comportamiento a través del integrador leapfrog se hacen iteraciones, para esto la computacion nos facilita y apresura el calculo requerido.

### variables requeridas por el código
como ya se dijo anteriormente el código requiere solamente de dos variables:

  >* velocidad inicial
  >* ángulo de lanzamiento

Luego el codigo simplemente se encargará él mismo de ver el tiempo mas efectivo, respetando las condiciones para que se complete a lo menos un ciclo 
### versiones de las librerias
numpy = 1.26.2
matplotlib = 3.5.1
