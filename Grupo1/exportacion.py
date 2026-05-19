import pandas as pd

def guardar_datos_limpios(df_limpio, ruta_salida="datos_reactor_limpio.csv"):
    """
    Función encargada de la Exportación de Datos.
    Recibe el DataFrame de Pandas ya filtrado (sin outliers) y lo guarda en un CSV nuevo.
    """
    try:
        df_limpio.to_csv(ruta_salida, index=False)
        print(f" Archivo purificado exportado con éxito en: '{ruta_salida}'")
        return True
    except Exception as e:
        print(f"No se pudo guardar el archivo CSV limpio: {e}")
        return False
