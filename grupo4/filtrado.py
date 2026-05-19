# Grupo 4
import numpy as np

def filtrar_outliers_3_sigma(datos_df, estadisticas):
    """
    Motor de filtrado matemático que descarta cualquier fila que esté
    por fuera del límite de 3 sigmas (media +/- 3*desviación).
    Recibe un DataFrame de Pandas y un diccionario de estadísticas.
    """
    
    # 1. Extraer a NumPy SOLO las columnas que vamos a evaluar
    # Esto evita errores si el CSV tiene una columna extra de "Tiempo" o "ID"
    matriz_valores = datos_df[['Temperatura', 'Presion']].to_numpy()

    # 2. Crear los arrays con las estadísticas
    medias = np.array([estadisticas['Temperatura']['media'], estadisticas['Presion']['media']])
    desviaciones = np.array([estadisticas['Temperatura']['std'], estadisticas['Presion']['std']])
    
    # 3. Calcular los límites (esto devuelve dos arrays [lim_temp, lim_pres])
    limite_inferior = medias - 3 * desviaciones
    limite_superior = medias + 3 * desviaciones
    
    # 4. Máscara booleana vectorizada eficiente en NumPy
    # Compara la matriz de Nx2 con los arrays de 1x2
    mascara_limpios = (matriz_valores >= limite_inferior) & (matriz_valores <= limite_superior)
    
    # np.all(axis=1) exige que TANTO la temperatura COMO la presión estén dentro del límite en esa fila
    mascara_final = np.all(mascara_limpios, axis=1)
        
    # 5. Retornar el DataFrame original (para no perder otras columnas) aplicando la máscara de NumPy
    # Pandas entiende perfectamente las máscaras booleanas creadas con NumPy
    return datos_df.iloc[mascara_final]
