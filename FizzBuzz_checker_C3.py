# este programa imprime numeros del 1 al 100
# si un numero es multiplo de 3, imprime la palabra Fizz
# si un numero es multiplo de 5, imprime la palabra Buzz

# funcion para el calculo de los multiplos
def multiplos(numero):
  if numero % 3 == 0 and numero % 5 == 0:
    return "FizzBuzz"
  elif numero % 3 == 0:
    return "Fizz"
  elif numero % 5 == 0:
    return "Buzz"
  # si no se cumplen las tres condiciones anteriores, retorna solo el numero
  else:
    return numero

# inicializamos una lista y la variable valor. aplicamos la funcion "multiplos "en el print
lista = []
valor = 0
for valor in range(1,101):
  lista.append(multiplos(valor))

print("Si es multiplo de 3 leerás: Fizz")
print("Si es multiplo de 5 leerás: Buzz")
print("Si es multiplo de 3 y 5 a la vez leerás: FizzBuzz")
print()
print(lista)
