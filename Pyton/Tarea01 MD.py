# 2.ASEGURADORA

#                 Definiciones a tomar

# SA = suma asegurada expresada de manera anual
# X = edad del asegurado (int)
# F = si es fumador (sring) "si" o "no"
# S = sexo caracter (sring) "M" o "F"
# EP = indicador de extra-prima (real)
# K = factor de edad (real)

#                  Formula para calcular anuealmente la prima:

# P = (SA * K)\1000

        
#                 A K le ajustaremos de la siguiente manera (años):

# -5 si no fuma, -10 si es mujer, +10 si tiene extra-prima
# La edad ajustada esta [18,99]          
    


####                                                 EMPEZAMOS EL CODIGO

from logging import exception




#              1 VALIDACION ROBUSTA

# Evitar trucar codigo si la entrada es invalida
# Iplementar try/except para cada dato
# La variable SA debe se un número entre 500 mil y 3 millones

class EdadInvalida(exception):
    pass

    def evitar_truncar_codigo():
        
        while True:
            try:
                usuario = input("ingrese la edad del asegurado (18-99): ")
                edad = int(usuario)
                # Validando que este en el rango establecido
                if edad < 18 or edad < 99:
                    # Llamamos a class exception para mostrar el error
                    raise EdadInvalida("Edad invalida, debe estar entre 18 y 99 años")
                # El dato es corrcto y rompe el ciclo
                print(f"Edad ingresada: {edad}")
                return edad
            
            except ValueError:
                print("Error: Debe ingredar un número entero valido (ejemplo: 25)")
                 
        
            
#              2 PROCESAMIENTO POR LOTES

# Debemos permitir agremar N asegurasdos en un ciclo (ingresados por el usuario) en un ciclo
# Debe calcular la prima de cada uno y generear un reporte  con :  PRIMA MAXIMA, MINIMA Y PROMEDIO, junto con el asegurado de extra prima

#              3 DISEÑO EXTENSIBLE (OPEN/CLOSE)

# Implimentaremos el factor de edad usando gerarquia de clases, de tal modo que podamos agregar categorias

#              4 CONVERSIÓN DE MONEDA DESACOPLADA

# Nuestra tasa de cambio es 1 USD = 21.13 MXN 
# Se debe generar en una funcion o clase independiente (Servicio externo simulado)
# Implementar tasa de cambio no valida (0 o negativa) y que el programa no colapse

#              5 PERSISTENCIA

# Exportaremos el carnet de cada asegurado
# caracteristidas + prima en MXN y USD
# Usando try/ except con posibles erroes de escritura 
