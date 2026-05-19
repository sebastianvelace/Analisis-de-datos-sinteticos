import numpy as np

def generar_dataset_reactor(nombre_archivo="datos_reactor.csv", n_muestras=5000):
    """Genera el CSV del reactor con un 2% de valores atipicos."""
    np.random.seed(42)

    temp_normal = np.random.normal(loc=180.0, scale=15.0, size=(n_muestras, 1))
    presion_normal = np.random.normal(loc=50.0, scale=5.0, size=(n_muestras, 1))
    datos_crudos = np.hstack((temp_normal, presion_normal))

    n_outliers = int(n_muestras * 0.02)
    indices_atipicos = np.random.choice(n_muestras, size=n_outliers, replace=False)
    datos_crudos[indices_atipicos, 0] += np.random.choice([150.0, -100.0], size=n_outliers)
    datos_crudos[indices_atipicos, 1] += np.random.choice([40.0, -30.0], size=n_outliers)

    encabezado = "Temperatura,Presion"
    np.savetxt(nombre_archivo, datos_crudos, delimiter=",", header=encabezado, comments="")
    print(f"Archivo generado: {nombre_archivo}")

if __name__ == "__main__":
    generar_dataset_reactor()
