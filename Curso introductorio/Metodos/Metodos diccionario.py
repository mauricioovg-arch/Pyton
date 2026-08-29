#Diccionarios

#Creacion de un diccionario
diccionario1 = {"nombre": "Juan", "edad": 30, "ciudad": "Madrid"}
dir(diccionario1) #Muestra los métodos disponibles para los diccionarios
"""Para usar un método, se escribe el nombre del diccionario seguido de un punto y el nombre del método"""

#En los diccionarios usasmos las clves para acceder a los valores, veamos algunos ejemplos:

"""Existen las siguientes formas de uso:
keys: Devuelve una lista con las claves del diccionario
get: Devuelve el valor de una clave específica, si la clave no existe devuelve None
clear: Elimina todos los elementos del diccionario
pop: Elimina un elemento del diccionario que pide la clave
items: Devuelve una lista de tuplas con las claves y valores del diccionario"""

#Ejemplo: Obtener las claves del diccionario
claves = diccionario1.keys() #Devuelve una lista con las claves del diccionario
#Ejemplo: Obtener el valor de una clave específica
valor = diccionario1.get("nombre") #Devuelve el valor de la clave "nombre"
#Ejemplo: Eliminar un elemento del diccionario que pide la clave
diccionario1.pop("edad") #Elimina el elemento con la clave "edad" del diccionario
#Ejemplo: Eliminar todos los elementos del diccionario
diccionario1.clear() #Elimina todos los elementos del diccionario
#Ejemplo: Obtener las claves y valores del diccionario
claves_valores = diccionario1.items() #Devuelve una lista de tuplas con las claves y valores del diccionario
