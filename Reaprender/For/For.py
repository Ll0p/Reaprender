# ¿ Qué es "for" ?

''' "for" es una estructura repetitiva (bucle) el cual, a diferencia de "while", no es infinito.
sino que esta definido su numero de repeticiones de antemano'''

# Método range: "range()" Es un método el cual genera una secuencia de numeros que van desde el cero hasta
# el número que le pasemos

# Podemos crear una lista de numeros:

lista_numeros = list(range(5))
print(lista_numeros) # --> [0, 1, 2, 3, 4]

# O tambien podemos transformar x valor a un rango:
rango = 5

for i in range(rango): # "I" vendria a ser la iteracion
    print(i) # --> 0 1 2 3 4 

# Este método tambien nos permite pasar 3 parametros seria

lista_numeros = list(range(10, 20, 2)) # 10 = inicio / 20 = fin / 2 = salto
print(lista_numeros) # [10, 12, 14, 16, 18]


# Método break: "break" Es una palabra reservada usada en un bucle con la cual DETENEMOS LA EJECUCIÓN DEL CÓDIGO.

for numero in range(5):
    print(numero)
    if numero == 2:
        break
print("FIN") # --> 0 1 2 FIN

# Método continue: "continue" Es una palabra reservada usada en un bucle con la cual SALTEAMOS UNA ITERECIÓN SIN DETENER EL CÓDIGO.

for numero in range(5):
    if numero == 2:
        continue
    print(numero) # 1
print("FIN") # --> 0 1 3 4 FIN