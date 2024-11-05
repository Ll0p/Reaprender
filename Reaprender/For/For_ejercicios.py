'''
1.Mostrar los números ascendentes desde el 1 al 10
2.Mostrar los números descendentes desde el 10 al 1
3.Ingresar un número. Mostrar los números desde 0 hasta el número ingresado.
4.Ingresar un número y mostrar la tabla de multiplicar de ese número. Por ejemplo si se ingresa el numero 5:

	5 x 0 = 0
	5 x 1  = 5
	5 x 2 = 10
	5 x 3  = 15 …

5.Se ingresan un máximo de 10 números o hasta que el usuario ingrese el número 0. Mostrar la suma y el promedio de todos los números.
6.Imprimir los números múltiplos de 3 entre el 1 y el 10 (*)
7.Mostrar los números pares que hay desde la unidad hasta el número 50 (*)
8.Realizar un programa que permita mostrar una pirámide de números. Por ejemplo: si se ingresa el numero 5, la salida del programa será la siguiente:


9.Ingresar un número. Mostrar todos los divisores que hay desde el 1 hasta el número ingresado. Mostrar la cantidad de divisores encontrados.
10.Ingresar un número. Determinar si el número es primo o no.
11.Ingresar un número. Mostrar cada número primo que hay entre el 1 y el número ingresado. Informar cuántos números primos se encontraron.'''

# 1.Mostrar los números ascendentes desde el 1 al 10

# for i in range(1, 11):
#     print(i)

# 2.Mostrar los números descendentes desde el 10 al 1

# for i in range(10, 0, -1):
#     print(i)

# 3.Ingresar un número. Mostrar los números desde 0 hasta el número ingresado.

# numero = int(input("Ingrese un número: "))

# for i in range(0, numero + 1):
#     print(i)

# 4.Ingresar un número y mostrar la tabla de multiplicar de ese número. Por ejemplo si se ingresa el numero 5:

# numero = int(input("Ingrese un número: "))

# for i in range(0, 11):
#     resultado = numero * i
#     print(f"{numero} x {i} = {resultado}")

# 5.Se ingresan un máximo de 10 números o hasta que el usuario ingrese el número 0. Mostrar la suma y el promedio de todos los números.

# acumulador = 0
# contador = 0

# for i in range(10):
#     numeros = int(input(f"[Numero {i+1}°] Ingrese un número: "))
#     if numeros == 0:
#         break
#     acumulador += numeros
#     contador += 1

# promedio = acumulador / contador
# print(f"La suma de todos los números es de: {acumulador}, y en promedio esto daria: {promedio}")

# 6.Imprimir los números múltiplos de 3 entre el 1 y el 10 (*)

# for i in range(0,11):
#     if i % 3 == 0:
#         print(i)

# 7.Mostrar los números pares que hay desde la unidad hasta el número 50 (*)

# for i in range(1, 51):
#     if i % 2 == 0:
#         print(i)

# 8.Realizar un programa que permita mostrar una pirámide de números. Por ejemplo: si se ingresa el numero 5, la salida del programa será la siguiente:

# numero = int(input("Ingrese un número: "))

# for i in range(0, numero + 1):
#     for j in range(i + 1):
#         print(j, end=" ")
#     print()

# 9.Ingresar un número. Mostrar todos los divisores que hay desde el 1 hasta el número ingresado. Mostrar la cantidad de divisores encontrados.

# numero = int(input("Ingrese un número y mostraremos todos los divisores de este: "))
# contador_divisores = 0 

# for i in range(1 ,numero + 1):
#     if numero % i == 0:
#         print(i)
#         contador_divisores += 1

# print(f"El total de divisores encontrados es de: {contador_divisores}")

# 10.Ingresar un número. Determinar si el número es primo o no.

# numero = int(input("Ingrese un número y determinaremos si es primo: "))
# es_primo = True

# if numero < 2:
#     es_primo = False
# else:
#     for i in range(2, numero):
#         if numero % i == 0:
#             es_primo = False
#             break

# if es_primo:
#     print(f"{numero} es un número primo.")
# else:
#     print(f"{numero} no es un número primo.")