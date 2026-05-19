import pandas as pd

def guardar_datos_limpios(df_limpio, ruta_salida="datos_reactor_limpio.csv"):
    """Guarda el DataFrame filtrado en un CSV."""
    try:
        df_limpio.to_csv(ruta_salida, index=False)
        print(f"CSV guardado: {ruta_salida}")
        return True
    except Exception as e:
        print(f"No se pudo guardar el CSV: {e}")
        return False
