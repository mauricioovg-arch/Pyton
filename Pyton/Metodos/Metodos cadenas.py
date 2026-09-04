#Cadenas
cadena1 = "Hola Mundo"
cadena2 = "Python es un lenguaje de programación"

dir(cadena1) #Muestra los métodos disponibles para las cadenas

"""Para usasr un método, se escribe el nombre de la cadena seguido de un punto y el nombre del método"""

#Ejemplo: Convertir la cadena a mayúsculas
cadena_mayusculas = cadena1.upper()
#Ejemplo: Convertir la cadena a minúsculas
cadena_minusculas = cadena1.lower()
#Ejemplo: Capitalizar la primera letra de cada palabra en la cadena
cadena_capitalizada = cadena1.title()

#Ejemplo:  buscar una palabra en la cadena
encontrar_palabra = cadena1.find("Mundo")
#Ejemplo: buscar una palabra con index
encontrar_palabra_index = cadena1.index("Mundo") 
"""La diferencia entre find e index es que find devuelve -1 si no encuentra la palabra, mientras que index lanza un error."""

#Para ver si un valor es numerico, se puede usar el método isnumeric
cadena_numerica = "12345"
es_numerica = cadena_numerica.isnumeric() #Devuelve True si la cadena es numerica, de lo contrario devuelve False
#Si el valr se alfa numerico, se puede usar el método isalnum
cadena_alfa_numerica = "Hola123"
es_alfa_numerica = cadena_alfa_numerica.isalnum() #Devuelve True si la cadena es alfa numerica, de lo contrario devuelve False

#Para buscar conicidencias en la cadena, se puede usar el método count
cadena_conicidencias = "Hola Mundo, Hola Python"
numero_conicidencias = cadena_conicidencias.count("Hola") #Devuelve el número de veces que aparece la palabra en la cadena
#Ejemplo: Contar el número de caracteres en la cadena
longitud_cadena = len(cadena1)

#Para verificar si una cadena comienza o termina con una palabra específica, se pueden usar los métodos startswith y endswith
cadena_inicio = cadena1.startswith("Hola") #Devuelve True si la cadena comienza con la palabra, de lo contrario devuelve False
cadena_final = cadena1.endswith("Mundo") #Devuelve True si la cadena termina con la palabra, de lo contrario devuelve False

#Para  Reemplazar una palabra en la cadena
cadena_reemplazada = cadena1.replace("Mundo", "Python")

#Para separar una cadena en una lista de palabras, se puede usar el método split
cadena_separada = cadena1.split() #Separa la cadena en una lista de palabras utilizando el espacio como separador
#Para unir una lista de palabras en una cadena, se puede usar el método join
lista_palabras = ["Hola", "Mundo"]
cadena_unida = " ".join(lista_palabras) #Une la lista de palabras en una cadena utilizando el espacio como separador



