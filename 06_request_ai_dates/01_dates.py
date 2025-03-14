# Trabajando con fechas y horas en Python

from datetime import datetime, timedelta
import locale

# Cambiar a español
locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')

# 1. Obtener la fecha y la hora actual
ahora = datetime.now()
print(f"Fecha y hora actual: {ahora}")

# 2. Crear una fecha y hora específica
fecha_especifica = datetime(2025, 1, 22, 23, 30)
print(f"Fecha y hora específica: {fecha_especifica}")

# 3. Formatear fechas
# método strftime() para formatear fechas
# pasarle el objeto datetime y el formato especificado
# formato:
formato_fecha = ahora.strftime("%d/%m/%Y %H:%M:%S")
print(f"Fecha formateada: {formato_fecha}")
print(f"Hoy es {ahora.strftime("%A %d de %B de %Y")}")

# 4. Operaciones con fechas (sumar/restar días, minutos, horas, meses)
ayer = ahora - timedelta(days=1)
print(f"Ayer: {ayer.strftime("%d/%m/%Y %H:%M:%S")}")

pasado_manana = ahora + timedelta(days=2)
print(f"Pasadomañana: {pasado_manana.strftime("%d/%m/%Y %H:%M:%S")}")

doce_horas_decimas = ahora - timedelta(days=0.5)
print(f"Menos medio día: {doce_horas_decimas.strftime("%d/%m/%Y %H:%M:%S")}")

# 5. Obtener componentes individuales de una fecha
annio = ahora.year
print(f"Año: {annio}")

mes = ahora.month
print(f"Mes: {mes}")

# 6. Calcular la diferencia entre 2 fechas
fecha1 = datetime.now()
fecha2 = datetime(2025, 6, 22)
diferencia = fecha2 - fecha1
print(f"Diferencia entre las dos fechas: {diferencia}")

