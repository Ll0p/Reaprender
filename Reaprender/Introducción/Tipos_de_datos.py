# Variables: Las variables son un objeto el cual contiene datos

variable_saludo = "hola"

# ¿ Qué tipos de datos puede tener una variable ?

numero_entero = 20
numero_flotante = 20.4
cadena_de_texto = "Hola buenos dias"
booleano = True

########## Como transformar los datos ##########

# Se usan lo que llamamos "Métodos" los cuales nos permiten transformar los tipos de datos y manipularlos (mas adelante se verá)
variable = 23

transformar_entero = int(variable) # --> 23
transformar_flotante = float(variable) # --> 23.00
transformar_cadena = str(variable) # --> "23"
# (tambien existe bool(), pero es irrelevante)

########## Mutable y no mutable ##########

# Objetos mutables: son aquellos que se pueden cambiar después de haber sido creados. 
# Esto significa que podés modificar el contenido de la variable sin crear una nueva referencia en memoria.

# Objetos inmutables: Los objetos inmutables no se pueden cambiar después de ser creados. 
# Cualquier "modificación" genera un nuevo objeto en memoria.

# Mutables: listas, diccionarios, sets y clases
# Inmutables: int, float, str, tuplas, frozensets