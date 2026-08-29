#Listas

#Crear una lista
lista1 = [1, 2, 3, 4, 5]
lista2 = ["Hola", "Mundo", "Python"]
dir(lista1) #Muestra los métodos disponibles para las listas
"""Para usar un método, se escribe el nombre de la lista seguido de un punto y el nombre del método"""

#Para contar la cantidad de elementos en la lista usaremos el método Len
longitud_lista1 = len(lista1) #Devuelve el número de elementos en la lista

#Para agregar un elemento a la lista en el indice especificado
lista1.insert(2, 10) #Agrega el elemento 10 en el índice 2 de la lista
#Para agregar un elemento a la lista
lista1.append(6) #Agrega el elemento 6 al final de la lista
#Para agregar varios elementos a la lista 
lista1.extend([7, 8, 9]) #Agrega los elementos 7, 8 y 9 al final de la lista

#Para  eliminar un elemento de una lista 
lista1.remove(10) #Elimina el elemento 10 de la lista
#Para eliminar un elemento de una lista que pide indice
lista1.pop(2) #Elimina el elemento en el índice 2 de la lista
#Para eliminar todos los elementos de una lista 
lista1.clear() #Elimina todos los elementos de la lista

#Para ordenar una lista de forma ascenddente 
lista1.sort() #Ordena la lista de forma ascendente
#Para invertir los elementos de una lista 
lista1.reverse() #Invierte el orden de los elementos de la lista

#En estas listas tambien podemos usar algunos metodos de las cadenas, veamos algunos ejemplos:

#Para contar el número de veces que aparece un elemento en la lista, se puede usar el método count
lista2 = ["Hola", "Mundo", "Python", "Hola"]
numero_conicidencias = lista2.count("Hola") #Devuelve el número de veces que aparece la palabra en la lista
#Para buscar el índice de un elemento en la lista, se puede usar el método index
indice_elemento = lista2.index("Mundo") #Devuelve el índice de la primera aparición de la palabra en la lista

#No es necesario hablar de los conjuntos pues son similares a las listas 