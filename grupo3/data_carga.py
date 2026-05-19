import pandas as pd

def cargar_datos(ruta_archivo):
    """Lee un CSV y devuelve un DataFrame o None si hay error."""
    try:
        df = pd.read_csv(ruta_archivo)

        if df.empty:
            print(f"Error: '{ruta_archivo}' no tiene filas de datos.")
            return None

        for col in df.columns:
            try:
                df[col] = pd.to_numeric(df[col], errors="raise")
            except ValueError:
                print(f"Error: valores no numericos en la columna '{col}'.")
                return None

        if df.isna().any().any():
            print(f"Error: hay valores faltantes en '{ruta_archivo}'.")
            return None

        print(f"Cargado: {ruta_archivo}")
        return df

    except FileNotFoundError:
        print(f"Error: no existe '{ruta_archivo}'.")
        return None

    except pd.errors.EmptyDataError:
        print(f"Error: '{ruta_archivo}' esta vacio.")
        return None

    except pd.errors.ParserError:
        print(f"Error: formato invalido en '{ruta_archivo}'.")
        return None

    except Exception as e:
        print(f"Error al cargar datos: {e}")
        return None
