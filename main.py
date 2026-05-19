from grupo3.data_carga import cargar_datos
from grupo2.estadisticas import calcular_estadisticas
from Grupo1.visualizacion import crear_graficas_comparativas
from Grupo1.exportacion import guardar_datos_limpios
from Grupo1.informe import generar_informe_pdf
from grupo4.generador import generar_dataset_reactor
from grupo4.filtrado import filtrar_outliers_3_sigma

def main():
    print("\n--- Generando datos ---")
    nombre_archivo_csv = "datos_reactor.csv"
    generar_dataset_reactor(nombre_archivo=nombre_archivo_csv, n_muestras=5000)

    print("\n--- Cargando datos ---")
    datos = cargar_datos(nombre_archivo_csv)
    if datos is not None:
        print("\n--- Estadisticas ---")
        estadisticas = calcular_estadisticas(datos)
        for col, s in estadisticas.items():
            print(f"  {col}: media={s['media']:.4f}, std={s['std']:.4f}, min={s['min']:.4f}, max={s['max']:.4f}")

        print("\n--- Filtrado (3 sigma) ---")
        datos_limpios = filtrar_outliers_3_sigma(datos, estadisticas)

        print("\n--- Exportacion y graficas ---")
        crear_graficas_comparativas(datos, datos_limpios)
        guardar_datos_limpios(datos_limpios, "datos_limpios_final.csv")
        generar_informe_pdf("informe_reactor.pdf", "comparativa_reactor.png")
        print("Listo.")
    else:
        print("\nNo se pudo cargar el archivo CSV.")

if __name__ == "__main__":
    main()
