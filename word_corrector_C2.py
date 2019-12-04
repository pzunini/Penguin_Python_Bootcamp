# Las dos últimas letras de cada palabra se traspusieron al principio.
# Este programa corrige las palabras e imprime la lista correctamente.

lista_mal = ['oscreem', 'ueq', 'la', 'óncodificaci', 'ñaense', 'eshabilidad', 'eld', 'losig', '21', 'osusam', 'la', 'óncodificaci', 'moco', 'nau', 'taherramien', 'rapa', 'armostr', 'moco']

# inicializamos lista para guardar las correcciones
lista_bien = []

# ciclo for que recorre la lista_mal
for palabra in lista_mal:
  # dividimos la palabra en dos partes
  parte2 = palabra[0:2] # parte que tiene las 2 primeras letras
  parte1 = palabra[2:len(palabra)] # parte que tiene el resto de las letras
  
  # agregamos cada palabra a la lista sumando las partes
  lista_bien.append(parte1 + parte2)

# imprimimos el mensaje uniendo las palabras de la lista
print("Mensaje: " + " ".join(lista_bien))

