#Importaciones desde los módulos separados por grupos
from grupo3.data_carga import cargar_datos
from grupo2.estadisticas import calcular_estadisticas
from Grupo1.visualizacion import crear_graficas_comparativas     
from Grupo1.exportacion import guardar_datos_limpios       
from grupo4.generador import generar_dataset_reactor
from grupo4.filtrado import filtrar_outliers_3_sigma

def main():
    print("\n--- Generando Datos Sintéticos ---")
    nombre_archivo_csv = "datos_reactor.csv"
    generar_dataset_reactor(nombre_archivo=nombre_archivo_csv, n_muestras=5000)
    print("Dataset de prueba generado.")
    # Cargamos los datos
    print("\n--- Cargando Datos ---")
    datos = cargar_datos(nombre_archivo_csv)
    if datos is not None:
        # Análisis Estadístico con la función de estadísticas.py
        print("\n--- Calculando Estadísticas ---")
        estadisticas = calcular_estadisticas(datos) 
        print("¡Estadísticas calculadas!")
        
        # Filtrado de Outliers 
        print("\n--- Filtrando Datos (Método 3 sigma) ---")
        datos_limpios = filtrar_outliers_3_sigma(datos, estadisticas)
        print("¡Valores atípicos filtrados!")
        
        # Visualización y Exportación 
        print("\n--- Generando Reportes y Exportando ---")
        # Aquí envías los datos finales a los archivos del Grupo 1
        crear_graficas_comparativas(datos, datos_limpios) # Del archivo visualizacion.py
        guardar_datos_limpios(datos_limpios, "datos_limpios_final.csv") # Del archivo exportacion.py
        print("¡Exportación y visualización finalizada!")
        
    else:
        #Se detendrá suavemente el programa aquí por el manejo de errores de data_carga.py
        print("\n El flujo se detuvo debido a un error en la carga de datos:(")

if __name__ == "__main__":
    main()
