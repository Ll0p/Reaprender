# ¿ Qué es una función ?

''' Una función es un bloque de codigo que realiza una tarea especifica (basicamente, pensa
una función como un mecanismo.)'''

# Estructura y ejemplo

def saludo(parametro: str) -> str: # Exijimos un parametro para hacer funcionar 
    "documentacion" # Nos sirve para saber que hace cada parte del código
    return parametro # Devuelve el valor (no siempre hay que usar un return)

saludito = "Hola"
print(saludo(parametro = saludito)) # Le pasamos el valor a los parametros

# ¿ Para que sirven las funciones ?

''' Las funciones son vitales para dividir nuestro codigo en tareas mas simples y hacer nuestro codigo
mas legible para todos '''

# Cosas a tener en cuenta: Las funciones es preferible que siempre se hagan genericas, esto con el proposito
# de hacerlas reutilizables para otras tareas y no tener que copiar codigo otra vez.

# ADEMAS, hay que tener en cuenta las variables.

# Variables locales: Las que están dentro de la función.
# Variables globales: Las que están fuera de la función.



