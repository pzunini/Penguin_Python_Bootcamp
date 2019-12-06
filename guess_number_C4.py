# Este juego genera un numero aleatorio entre dos numeros introducidos por el usuario
# El usuario debe adivinar introduciendo un tercer numero que esté dentro del rango de los anteriores dos.  

import random

# solicitamos el rango de numeros al usuario
a = int(input("Introduza el rango inferior: "))
b = int(input("Introduza el rango superior: "))

# generamos el numero aleatorio e inicializamos la cantidad de intentos
random_num = random.randint(a, b)
intentos = 1

# creamos un ciclo que se repira hasta que el usuario adivine
while True:
  # solicitamos al usuario un numero
  num = int(input("Introduza un numero y adivine: "))

  # verificamos que el numero introducido se encuentre dentro del rango establecido
  if num < a or num > b:
    print("El numero debe estar dentro del rango! Pruebe otra vez")
  else:
    if num != random_num:
      if num < random_num:
        print("Lo siento, ¡inténtalo de nuevo! Muy bajo")
      if num > random_num:
        print("Lo siento, ¡inténtalo de nuevo! Muy alto")
      intentos = intentos + 1
    else:
      print("¡Felicidades! Lo has adivinado en el intento", intentos)
      break
