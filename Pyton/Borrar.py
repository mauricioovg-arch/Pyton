# 1. Definimos nuestra propia excepción (alarma) heredando de Exception
class EdadInvalidaError(Exception):
    """Error personalizado para edades fuera del rango permitido [18, 99]."""
    pass

# 2. Creamos la función que funcionará como nuestro 'cadenero'
def capturar_edad():
    """Solicita la edad al usuario y fuerza un ciclo hasta que el dato sea válido."""
    
    # Este ciclo repetirá la pregunta infinitamente hasta que el dato sea correcto
    while True:
        try:
            # input() pide texto al usuario. int() intenta convertir ese texto a un número entero.
            entrada_usuario = input("Ingresa la edad del asegurado (18-99): ")
            edad = int(entrada_usuario)
            
            # Verificamos si la edad rompe la regla de la aseguradora
            if edad < 18 or edad > 99:
                # 'raise' activa nuestra alarma personalizada si el dato es incorrecto
                raise EdadInvalidaError("La edad debe estar estrictamente entre 18 y 99 años.")
            
            # Si el código llega a esta línea, el dato es perfecto. 
            # 'return' devuelve el valor y rompe el ciclo 'while'.
            print(f"¡Dato aceptado! Edad registrada: {edad}")
            return edad
            
        except ValueError:
            # Se activa si el usuario escribe letras (ej. "veinte") en lugar de números
            print("Error: Por favor, ingresa un número entero válido (ejemplo: 25).")
            
        except EdadInvalidaError as error_personalizado:
            # Se activa si nuestro 'raise' sonó la alarma por una edad fuera de rango
            print(f"Aviso de negocio: {error_personalizado}")

# 1. Nuevas excepciones (alarmas) personalizadas
class SumaAseguradaInvalidaError(Exception):
    """Error para montos fuera del rango de 500,000 a 3,000,000."""
    pass

class OpcionInvalidaError(Exception):
    """Error para textos que no coinciden con las opciones permitidas."""
    pass

# 2. Función para capturar el dinero
def capturar_suma_asegurada():
    """Pide el dinero y valida que sea un decimal en el rango correcto."""
    while True:
        try:
            # float() intenta convertir el texto a un número con decimales
            entrada = input("Ingresa la suma asegurada ($500,000 - $3,000,000): ")
            suma = float(entrada)
            
            # Verificamos los límites del negocio
            if suma < 500000.0 or suma > 3000000.0:
                raise SumaAseguradaInvalidaError("El monto debe estar entre 500,000 y 3,000,000 MXN.")
            
            print(f"¡Monto aceptado! ${suma}")
            return suma
            
        except ValueError:
            # Si el usuario escribe "medio millón" con letras
            print("Error: Ingresa una cantidad numérica válida (ejemplo: 1500000).")
            
        except SumaAseguradaInvalidaError as error:
            print(f"Aviso de negocio: {error}")

# 3. Función 'comodín' para capturar opciones de texto
def capturar_opcion(mensaje, opciones_validas):
    """Pide un texto y verifica que exista dentro de la lista de opciones válidas."""
    while True:
        try:
            # Le pedimos el dato al usuario.
            # .strip() borra espacios accidentales al inicio/final.
            # .capitalize() asegura que la primera letra sea mayúscula (ej. 'si' -> 'Si').
            entrada = input(f"{mensaje} ({'/'.join(opciones_validas)}): ").strip().capitalize()
            
            # Revisamos si lo que escribió NO está en nuestra lista de permitidos
            if entrada not in opciones_validas:
                raise OpcionInvalidaError(f"Debes ingresar exactamente una de estas opciones: {opciones_validas}")
            
            return entrada
            
        except OpcionInvalidaError as error:
            print(f"Error de entrada: {error}")
            
class Asegurado:
    """Molde principal para registrar clientes y procesar su riesgo."""

    def __init__(self, edad, sexo, fumador, extra_prima, suma_asegurada):
        # Guardamos los datos validados como atributos propios del objeto
        self.edad = edad
        self.sexo = sexo
        self.fumador = fumador
        self.extra_prima = extra_prima
        self.suma_asegurada = suma_asegurada

    def obtener_edad_ajustada(self):
        """Aplica las reglas de negocio para determinar la edad de riesgo."""
        # Tomamos la edad real como punto de partida
        edad_riesgo = self.edad
        
        # Aplicamos las bonificaciones y penalizaciones
        if self.sexo == 'F':
            edad_riesgo -= 10
            
        if self.fumador == 'No':
            edad_riesgo -= 5
            
        if self.extra_prima == 'Si':
            edad_riesgo += 10
            
        # Acotamos el resultado para no salirnos de los límites
        if edad_riesgo < 18:
            return 18
        elif edad_riesgo > 99:
            return 99
        else:
            return edad_riesgo
# Importamos las herramientas de Python para crear clases abstractas
from abc import ABC, abstractmethod

# --- EL CONTRATO BASE ---
class FactorEdadStrategy(ABC):
    """Plantilla maestra. Obliga a las subclases a tener el método obtener_factor."""
    
    @abstractmethod
    def obtener_factor(self, edad_ajustada):
        pass

# --- LOS CARTUCHOS INTERCAMBIABLES ---
class FactorFemenino(FactorEdadStrategy):
    """Contiene la tabla matemática exclusiva para el sexo femenino."""
    
    def obtener_factor(self, edad_ajustada):
        if 18 <= edad_ajustada <= 25:
            return 1.5
        elif 26 <= edad_ajustada <= 45:
            return 1.7
        elif 46 <= edad_ajustada <= 65:
            return 2.0
        else: # Cubre de 66 a 99 años
            return 2.2

class FactorMasculino(FactorEdadStrategy):
    """Contiene la tabla matemática exclusiva para el sexo masculino."""
    
    def obtener_factor(self, edad_ajustada):
        if 18 <= edad_ajustada <= 25:
            return 2.0
        elif 26 <= edad_ajustada <= 45:
            return 2.3
        elif 46 <= edad_ajustada <= 65:
            return 2.5
        else: # Cubre de 66 a 99 años
            return 3.0
# 1. Agrega esta excepción junto a las otras (EdadInvalidaError, etc.)
class TasaCambioInvalidaError(Exception):
    """Error activado cuando la tasa de cambio es cero o negativa."""
    pass

# 2. Clase independiente simulando un servicio web
class ServicioCambioMoneda:
    """Módulo desacoplado para consultar el precio del dólar."""
    
    def __init__(self, tasa_simulada=21.13):
        # Guardamos la tasa de cambio dictada por el ejercicio
        self.tasa_actual = tasa_simulada
        
    def obtener_tasa_usd(self):
        """Devuelve la tasa verificando primero que sea válida."""
        try:
            # Una tasa de cambio en la vida real no puede ser negativa ni gratis (cero)
            if self.tasa_actual <= 0:
                raise TasaCambioInvalidaError("La tasa de cambio no puede ser cero ni negativa.")
            
            return self.tasa_actual
            
        except TasaCambioInvalidaError as error_moneda:
            # El sistema atrapa el error y lo muestra en pantalla
            print(f"Alerta de conexión externa: {error_moneda}")
            # Devolvemos None (nada) para indicar que falló la consulta
            return None
def procesar_lote_asegurados():
    """Motor principal que procesa clientes, calcula primas y genera archivos."""
    try:
        n_clientes = int(input("¿Cuántos asegurados procesaremos hoy?: "))
    except ValueError:
        print("Cantidad inválida. Asignando 1 cliente por defecto.")
        n_clientes = 1

    # Variables para rastrear las estadísticas finales
    suma_primas = 0.0
    prima_maxima = 0.0
    prima_minima = float('inf')  # Empezamos con infinito para que el primer valor lo reemplace
    
    # Encendemos nuestro servicio independiente de conversión de dólares
    servicio_usd = ServicioCambioMoneda()
    tasa_dolar = servicio_usd.obtener_tasa_usd()

    # Abrimos el archivo protegiéndolo de fallos físicos
    try:
        # 'w' abre el archivo en modo escritura (write)
        with open("carnet_asegurados.txt", "w") as archivo:
            archivo.write("--- REGISTRO OFICIAL DE ASEGURADOS ---\n\n")
            
            for i in range(n_clientes):
                print(f"\n=== Procesando Cliente {i + 1} de {n_clientes} ===")
                
                # 1. Validación robusta (Usamos nuestros cadeneros)
                edad = capturar_edad()
                sexo = capturar_opcion("Sexo", ["M", "F"])
                fumador = capturar_opcion("Fumador", ["Si", "No"])
                ep = capturar_opcion("Extra-prima", ["Si", "No"])
                sa = capturar_suma_asegurada()
                
                # 2. Creamos el objeto Asegurado
                cliente = Asegurado(edad, sexo, fumador, ep, sa)
                edad_ajustada = cliente.obtener_edad_ajustada()
                
                # 3. Diseño Extensible (Elegimos el cartucho de tarifa)
                if sexo == 'F':
                    estrategia = FactorFemenino()
                else:
                    estrategia = FactorMasculino()
                    
                factor_k = estrategia.obtener_factor(edad_ajustada)
                
                # 4. Cálculo de la Prima Anual
                prima_mxn = (sa * factor_k) / 1000
                
                # 5. Persistencia (Guardamos en el disco duro)
                archivo.write(f"CLIENTE {i + 1}\n")
                archivo.write(f"Edad Real: {edad} | Edad Riesgo: {edad_ajustada} | Sexo: {sexo}\n")
                archivo.write(f"Fumador: {fumador} | Extra-prima: {ep}\n")
                archivo.write(f"Suma Asegurada: ${sa:,.2f} MXN\n")
                archivo.write(f"PRIMA A PAGAR: ${prima_mxn:,.2f} MXN\n")
                
                if tasa_dolar is not None:
                    prima_usd = prima_mxn / tasa_dolar
                    archivo.write(f"PRIMA EN DÓLARES: ${prima_usd:,.2f} USD\n")
                    
                archivo.write("-" * 40 + "\n")
                
                # 6. Actualización de estadísticas
                suma_primas += prima_mxn
                if prima_mxn > prima_maxima:
                    prima_maxima = prima_mxn
                if prima_mxn < prima_minima:
                    prima_minima = prima_mxn

        print("\n¡Proceso exitoso! Los carnets se exportaron a 'carnet_asegurados.txt'.")
        
    except IOError as e:
        # Esto nos salva si hay un error de permisos o ruta en la computadora
        print(f"\nError de escritura crítico: No se pudo guardar el archivo. Detalle: {e}")

    # Mostrar reporte final
    if n_clientes > 0:
        print("\n=== REPORTE FINAL DE LOTES ===")
        print(f"Prima Promedio: ${suma_primas / n_clientes:,.2f} MXN")
        print(f"Prima Máxima Registrada: ${prima_maxima:,.2f} MXN")
        print(f"Prima Mínima Registrada: ${prima_minima:,.2f} MXN")

# Con esto arranca todo tu programa
if __name__ == "__main__":
    procesar_lote_asegurados()