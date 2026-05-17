import numpy as np

def filtrar_outliers_3_sigma(datos_crudos, media, desviacion):
    """
    Motor de filtrado matemático que descarta cualquier fila que esté
    por fuera del límite de 3 sigmas (media +/- 3*desviación).
    """
    limite_inferior = media - 3 * desviacion
    limite_superior = media + 3 * desviacion
    
    # Máscara booleana vectorizada eficiente
    mascara_limpios = (datos_crudos >= limite_inferior) & (datos_crudos <= limite_superior)
    
    if datos_crudos.ndim > 1:
        mascara_limpios = np.all(mascara_limpios, axis=1)
        
    # Retorna los datos purgados
    return datos_crudos[mascara_limpios]