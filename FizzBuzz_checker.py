# este programa imprime numeros del 1 al 100
# si un numero es multiplo de 3, imprime la palabra Fizz
# si un numero es multiplo de 5, imprime la palabra Buzz

# funcion para el calculo de los multiplos
def multiplos(numero):
  if numero % 3 == 0:
    return "Fizz"
  elif numero % 5 == 0:
    return "Buzz"
  # si no se cumplen las dos condiciones anteriores, retorna solo el numero
  else:
    return numero

# inicializamos la variable valor y aplicamos la funcion "multiplos "en el print
valor = 0
for valor in range(-50,50):
  print(multiplos(valor))
