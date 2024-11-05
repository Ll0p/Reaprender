'''UTN Technologies, una reconocida software factory se encuentra en la búsqueda de ideas para su próximo desarrollo en Python, que promete revolucionar el mercado.

Las posibles aplicaciones son las siguientes:
Inteligencia artificial (IA),
Realidad virtual/aumentada (RV/RA),
Internet de las cosas (IOT)

Para ello, la empresa realiza entre sus empleados una encuesta, con el propósito de conocer ciertas métricas.

A) Los datos a ingresar por cada empleado encuestado son:
nombre del empleado
edad (no menor a 18)
género (Masculino - Femenino - Otro)
tecnologia (IA, RV/RA, IOT)  
B) Cargar por terminal 10 encuestas.
C) Determinar:
Cantidad de empleados de género masculino que votaron por IOT o IA, cuya edad esté entre 25 y 50 años inclusive.
Porcentaje de empleados que no votaron por IA, siempre y cuando su género no sea Femenino o su edad se encuentre entre los 33 y 40.
Nombre y tecnología que votó, de los empleados de género masculino con mayor edad de ese género.'''

contador = 0
cantidad_empleados = 10  # Cargar por terminal 10 encuestas
cantidad_m_ia_iot_25_50 = 0
cantidad_no_ia_f_33_40 = 0

# Inicializamos variables para el empleado masculino de mayor edad
edad_mayor = 0
tecnologia_votada_x_mayor = None
nombre_mayor = None

while contador < cantidad_empleados:
    edad = int(input(f"[Empleado {contador + 1}] Ingrese su edad: "))
    if edad < 18:
        print("Usted es menor, no puede votar.")
        continue
    nombre = input(f"[Empleado {contador + 1}] Ingrese su nombre: ")
    genero = input(f"[Empleado {contador + 1}] Ingrese su género [M/F/O]: ").upper()
    while genero != "M" and genero != "F" and genero != "O":
        print("Género no validado, ingrese una opción válida (M/F/O).")
        genero = input(f"[Empleado {contador + 1}] Ingrese su género [M/F/O]: ").upper()

    tecnologia = input(f"[Empleado {contador + 1}] Indique su voto [IA/RV/IOT]: ").upper()
    while tecnologia != "IA" and tecnologia != "RV" and tecnologia != "IOT":
        print("Voto invalidado, ingrese una de opción válida (IA/RV/IOT).")
        tecnologia = input(f"[Empleado {contador + 1}] Indique su voto [IA/RV/IOT]: ").upper()

    if genero == "M" and (tecnologia == "IA" or tecnologia == "IOT") and (edad >= 25 and edad <= 50):
        cantidad_m_ia_iot_25_50 += 1

    if tecnologia != "IA" and genero != "F" and (edad >= 33 and edad <= 40):
        cantidad_no_ia_f_33_40 += 1

    if genero == "M" and edad > edad_mayor:
        edad_mayor = edad
        tecnologia_votada_x_mayor = tecnologia
        nombre_mayor = nombre

    contador += 1

print(f"Cantidad de empleados de género masculino que votaron por IOT o IA, cuya edad está entre 25 y 50 años: {cantidad_m_ia_iot_25_50}")
print(f"Cantidad de empleados que no votaron por IA y cumplen las condiciones: {cantidad_no_ia_f_33_40}")
if nombre_mayor:
    print(f"Nombre y tecnología votada del empleado masculino de mayor edad: {nombre_mayor}, {tecnologia_votada_x_mayor}")
else:
    print("No se registraron empleados masculinos.")
