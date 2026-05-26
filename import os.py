import os

# Prefijo con nombre y apellido
prefijo = "Bastian_Campos"

# Obtener lista de archivos .log en el directorio actual
archivos_log = [f for f in os.listdir('.') if f.endswith('.log')]

# Ordenar alfabéticamente (opcional, para consistencia)
archivos_log.sort()

# Contador incremental
contador = 1

# Renombrar cada archivo
for archivo in archivos_log:
    nuevo_nombre = f"{prefijo}_{contador}.log"
    ruta_original = os.path.join('.', archivo)
    ruta_nueva = os.path.join('.', nuevo_nombre)
    os.rename(ruta_original, ruta_nueva)
    print(f"Renombrado: {archivo} -> {nuevo_nombre}")
    contador += 1

if contador == 1:
    print("No se encontraron archivos .log en el directorio actual.")
else:
    print(f"Proceso completado. Se renombraron {contador-1} archivos.")