from data_carga import cargar_datos

# Importaciones desde las carpetas de los demás grupos
from grupo2.estadisticas import calcular_estadisticas
from Grupo1.visualizacion import generar_graficas     
from Grupo1.exportacion import exportar_datos         

# Importación pendiente del Grupo 4
# from grupo4.filtrado import filtrar_outliers

def main():
    print("--- Iniciando Sistema de Procesamiento de Datos ---")
    
    # Carga de datos
    # Aquí iría la ruta del CSV sintético generado por el Grupo 4
    ruta_csv = "../grupo4/datos_sinteticos.csv" 
    datos = cargar_datos(ruta_csv)
    
    if datos is not None:
        
        # 2. Análisis Estadístico (Grupo 2)
        print("\n--- Calculando Estadísticas ---")
        # Aquí le pasas tus datos cargados al archivo estadisticas.py del Grupo 2
        estadisticas = calcular_estadisticas(datos) 
        print("¡Estadísticas calculadas!")
        
        # Filtrado de Outliers 
        print("\n--- Filtrando Datos ---")
    
        # datos_limpios = filtrar_outliers(datos, estadisticas)
        print("¡Datos filtrados!")
        
        # Visualización y Exportación 
        print("\n--- Generando Reportes y Exportando ---")
        # Aquí envías los datos finales a los archivos del Grupo 1
        generar_graficas(datos, datos_limpios) # Del archivo visualizacion.py
        exportar_datos(datos_limpios, "datos_limpios_final.csv") # Del archivo exportacion.py
        print("¡Exportación y visualización finalizada!")
        
    else:
        print("\n El flujo se detuvo debido a un error en la carga :(")

if __name__ == "__main__":
    main()
