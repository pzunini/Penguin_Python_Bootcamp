# Este juego genera un numero aleatorio entre 1 y 100 y
# el usuario debe adivinar introduciendo un numero cualquiera. 

# generamos el numero aleatorio
import random
def generador(x, y):
  random_num = random.randint(x, y)
  return random_num

# solicitamos el rango de numeros al usuario
a = int(input("Introduza el rango inferior: "))
b = int(input("Introduza el rango superior: "))

# llamamos a la funcion con los numeros ingresados por el usuario
gen = generador(a, b)

# guardamos la cantidad de intentos del usuario.
intentos = 1

# creamos un ciclo que se repira hasta que el usuario adivine
while True:
  # solicitamos al usuario un numero
  num = int(input("Introduza un numero y adivine: "))

  # verificamos que el numero introducido se encuentre dentro del rango establecido
  if num < a or num > b:
    print("El numero debe estar dentro del rango! Pruebe otra vez")
  else:
    if num != gen:
      if num < gen:
        print("Lo siento, ¡inténtalo de nuevo! Muy bajo")
      if num > gen:
        print("Lo siento, ¡inténtalo de nuevo! Muy alto")
      intentos = intentos + 1
    else:
      print("¡Felicidades! Lo has adivinado en el intento", intentos)
      break
