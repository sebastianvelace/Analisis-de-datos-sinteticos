# Grupo 4

import numpy as np
import pandas as pd
from grupo2.estadisticas import calcular_estadisticas

datos_crudos = pd.read_csv('datos_reactor.csv')
estadisticas = calcular_estadisticas(datos_crudos)
raw_data = 'datos_reactor.csv'
def filtrar_outliers_3_sigma(raw_data, estadisticas):
    """
    Motor de filtrado matemático que descarta cualquier fila que esté
    por fuera del límite de 3 sigmas (media +/- 3*desviación).
    """
    crudos = np.genfromtxt(raw_data, delimiter=",", skip_header=1)

    '''
    Creo 2 arrays uno con las medias de nuestras dos medidas y otro
    con la desvaición de las dos medidas ya quw podemos operar entre arrays
    '''
    medias = np.array([estadisticas['Temperatura']['media'], estadisticas['Presion']['media']])
    desviaciones = np.array([estadisticas['Temperatura']['std'], estadisticas['Presion']['std']])
    
    '''
    El resultado de estos limites van a ser dos arrays [temperatura,presion]

    '''
    limite_inferior = medias - 3 * desviaciones
    limite_superior = medias + 3 * desviaciones
    
    # Máscara booleana vectorizada eficiente
    #Compara toda la matriz con los arrays obetnidos anteriormente 
    mascara_limpios = (crudos >= limite_inferior) & (crudos <= limite_superior)
    
    if crudos.ndim > 1:
        mascara_limpios = np.all(mascara_limpios, axis=1)
        
    # Retorna los datos purgados
    return crudos[mascara_limpios]