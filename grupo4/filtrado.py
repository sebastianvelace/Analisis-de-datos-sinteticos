import numpy as np

def filtrar_outliers_3_sigma(datos_df, estadisticas):
    """Filtra filas fuera de media +/- 3 * desviacion estandar."""
    matriz_valores = datos_df[['Temperatura', 'Presion']].to_numpy()

    medias = np.array([estadisticas['Temperatura']['media'], estadisticas['Presion']['media']])
    desviaciones = np.array([estadisticas['Temperatura']['std'], estadisticas['Presion']['std']])

    limite_inferior = medias - 3 * desviaciones
    limite_superior = medias + 3 * desviaciones

    mascara_limpios = (matriz_valores >= limite_inferior) & (matriz_valores <= limite_superior)
    mascara_final = np.all(mascara_limpios, axis=1)

    return datos_df.iloc[mascara_final]
