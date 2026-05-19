import pandas as pd

def cargar_datos(ruta_archivo):
    """
    Carga los datos de un archivo CSV y maneja posibles errores.
    """
    try:
        # Intentamos leer el archivo CSV
        df = pd.read_csv(ruta_archivo)
        print(f"Éxito: Datos cargados correctamente desde '{ruta_archivo}'.")
        return df
        
    except FileNotFoundError:
        # Capturamos si la ruta está mal o el archivo no existe
        print(f"Error de archivo: No se encontró el archivo en la ruta '{ruta_archivo}'. Verifica el nombre o la ubicación del mismo.")
        return None
        
    except pd.errors.EmptyDataError:
        # Capturamos si el archivo está vacío
        print(f"Error de formato: El archivo '{ruta_archivo}' está vacío.")
        return None
        
    except pd.errors.ParserError:
        # Capturamos si hay errores de formato (ej. letras en vez de números estructurados)
        print(f"Error de lectura: El archivo '{ruta_archivo}' tiene un formato corrupto o términos irregulares.")
        return None
        
    except Exception as e:
        # Capturamos cualquier otro error inesperado
        print(f"Error inesperado al cargar los datos: {e}")
        return None
