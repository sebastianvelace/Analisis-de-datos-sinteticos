import numpy as np

def generar_dataset_videos(nombre_archivo="youtube_completo.csv", n_muestras=5000):
    """
    Fabricación del dataset original inyectando un 2% de valores 
    atípicos artificiales usando numpy.random.
    """
    np.random.seed(42) # Replicabilidad
    
    # Simular un comportamiento de vistas normal estructurado
    vistas_normales = np.random.normal(loc=50000, scale=15000, size=(n_muestras, 1))
    vistas_normales = np.clip(vistas_normales, 0, None) # Evitar números negativos
    
    # Inyectar outliers artificiales exagerados (ruido en el experimento)
    n_outliers = int(n_muestras * 0.02)
    indices_atipicos = np.random.choice(n_muestras, size=n_outliers, replace=False)
    vistas_normales[indices_atipicos] += np.random.choice([300000, 600000], size=n_outliers, replace=True).reshape(-1, 1)
    
    # Guardar en la raíz del proyecto
    np.txt_data = vistas_normales
    np.savetxt(nombre_archivo, vistas_normales, delimiter=",", header="Vistas", comments="")
    print(f"\n[Grupo 4] Dataset sintético generado con éxito en: '{nombre_archivo}'")

if __name__ == "__main__":
    generar_dataset_videos()