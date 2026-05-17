import csv
import os

def ver_historial_interfaz(archivo_csv="historial.csv"):
    """
    Lee el archivo CSV de consultas y lo despliega ordenadamente 
    como una tabla dinámica en la terminal de la interfaz.
    """
    if not os.path.exists(archivo_csv) or os.path.getsize(archivo_csv) == 0:
        print("\n[📁] El historial está vacío o el archivo 'historial.csv' no se ha generado.")
        return

    print("\n" + "="*75)
    print("📜 INTERFAZ DE CONTROL: HISTORIAL DE CONSULTAS OBLIGATORIO")
    print("="*75)
    print(f"{'FECHA Y HORA'.ljust(18)} | {'OPCIÓN INGRESADA / ACCIÓN'.ljust(35)} | {'REF CANTIDAD'}")
    print("-"*75)

    with open(archivo_csv, "r", encoding="utf-8") as archivo:
        lector = csv.reader(archivo)
        for fila in lector:
            if len(fila) == 3:
                fecha, entrada, num_entrada = fila
                print(f"{fecha.ljust(18)} | {entrada.ljust(35)} | {num_entrada}")
                
    print("="*75 + "\n")