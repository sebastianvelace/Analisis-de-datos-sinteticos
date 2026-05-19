import numpy as np
import pandas as pd

datos= 'datos_reactor.csv'
def calcular_estadisticas(datos: pd.DataFrame) -> dict:
    columnas_numericas = datos.select_dtypes(include=[np.number]).columns
    resultado = {}


    for col in columnas_numericas:
        valores = datos[col].to_numpy()
        resultado[col] = {
           "media": np.mean(valores),
           "std": np.std(valores),
           "max": np.max(valores),
           "min": np.min(valores),
        }

    return resultado