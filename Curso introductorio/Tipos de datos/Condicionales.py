#Son pedazos de código que se ejecutan solo si se cumple una condición específica. Se utilizan para tomar decisiones en el programa y controlar el flujo de ejecución.
"""
Los condicionales son los siguientes:
- if: Se ejecuta un bloque de código si se cumple una condición. Ejemplo:
if edad >= 18:
    print("Eres mayor de edad")
- else: Se ejecuta un bloque de código si no se cumple la condición del if. Ejemplo:
if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")
- elif: Se utiliza para agregar condiciones adicionales después de un if. Ejemplo:
if edad < 18:       
    print("Eres menor de edad")
elif edad >= 18 and edad < 65:
    print("Eres adulto")
else:
    print("Eres adulto mayor")
    
"""
#También existen los operadores lógicos (and, or, not) que se utilizan para combinar condiciones en los condicionales.
"""
- and: Devuelve True si ambas condiciones son verdaderas. Ejemplo:
if edad >= 18 and edad < 65:
    print("Eres adulto")
- or: Devuelve True si al menos una de las condiciones es verdadera. Ejemplo:
if edad < 18 or edad >= 65:
    print("Eres menor de edad o adulto mayor")
- not: Devuelve True si la condición es falsa. Ejemplo:
if not es_estudiante:
    print("No eres estudiante")
"""
