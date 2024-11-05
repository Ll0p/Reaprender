# ¿ Qué es un módulo ?

''' Un "módulo" es un archivo en el cual vamos a contener varias funciones. Esto
con la necesidad de tener un mejor mantenimiento del codigo y poder usarlas en otros modulos'''

# ¿ Qué es un paquete ?

''' Un "paquete" vendria a ser una carpeta en la cual tenemos modulos dentro. Obviamente, dentro de 
cada carpeta vamos a tener cosas que tengan por lo menos algo de similitud'''

# Ejemplo:

# Esto funcionaria si metieramos la carpeta "Funciones" DENTRO de al carpeta "Modulos y paquetes"
# (pero no lo voy a hacer)
from Funciones.Funcion import saludo

saludazo = "Hola buen dia"
saludo(parametro = saludazo)