import numpy as np

def generar_dataset_reactor(nombre_archivo="datos_reactor.csv", n_muestras=5000):
    """
    Fabricación del dataset original para el reactor químico,
    inyectando un 2% de valores atípicos artificiales usando numpy.random.
    """
    np.random.seed(42)  # Replicabilidad del experimento

    # 1. Simular comportamiento normal estructurado (Distribución Normal)
    # Temperatura promedio: 180°C con desviación de 15°C
    temp_normal = np.random.normal(loc=180.0, scale=15.0, size=(n_muestras, 1))
    
    # Presión promedio: 50 psi con desviación de 5 psi
    presion_normal = np.random.normal(loc=50.0, scale=5.0, size=(n_muestras, 1))
    
    # Concatenar horizontalmente para crear una matriz de (n_muestras, 2)
    datos_crudos = np.hstack((temp_normal, presion_normal))

    # 2. Inyectar outliers artificiales exagerados (2% de ruido en el experimento)
    n_outliers = int(n_muestras * 0.02)
    
    # Elegir filas aleatorias donde meteremos los ruidos
    indices_atipicos = np.random.choice(n_muestras, size=n_outliers, replace=False)
    
    # Inyectar anomalías (valores extremadamente altos o bajos)
    # Para Temperatura: sumamos o restamos picos enormes (ej. +150°C o -100°C)
    datos_crudos[indices_atipicos, 0] += np.random.choice([150.0, -100.0], size=n_outliers)
    
    # Para Presión: sumamos o restamos picos proporcionales (ej. +40 psi o -30 psi)
    datos_crudos[indices_atipicos, 1] += np.random.choice([40.0, -30.0], size=n_outliers)

    # 3. Guardar en la raíz del proyecto con encabezados claros
    encabezado = "Temperatura,Presion"
    np.savetxt(nombre_archivo, datos_crudos, delimiter=",", header=encabezado, comments="")
    
    print(f"\n[Grupo 4] Dataset sintético del reactor generado con éxito en: '{nombre_archivo}'")

if __name__ == "__main__":
    generar_dataset_reactor()
