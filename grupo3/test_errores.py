import os
from data_carga import cargar_datos

def ejecutar_pruebas_qa():
    print("="*60)
    print(" INICIANDO PRUEBAS DE ESTRÉS Y CONTROL DE EXCEPCIONES... ")
    print("="*60)

    # ---------------------------------------------------------
    # PRUEBA 1: Archivo inexistente (FileNotFoundError)
    # ---------------------------------------------------------
    print("\n[Prueba 1] Simulando lectura de un archivo que no existe...")
    ruta_falsa = "ruta_inventada/datos_que_no_existen.csv"
    datos_1 = cargar_datos(ruta_falsa)
    assert datos_1 is None, "Error: La función debió retornar None."

    # ---------------------------------------------------------
    # PRUEBA 2: Archivo completamente vacío (EmptyDataError)
    # ---------------------------------------------------------
    print("\n[Prueba 2] Simulando lectura de un archivo completamente vacío...")
    ruta_vacia = "archivo_vacio_temp.csv"
    
    # Creamos un archivo vacío temporal
    open(ruta_vacia, 'w').close() 
    
    # Probamos la función
    datos_2 = cargar_datos(ruta_vacia)
    assert datos_2 is None, "Error: La función debió retornar None."
    
    # Limpiamos el archivo temporal
    os.remove(ruta_vacia)

    # ---------------------------------------------------------
    # PRUEBA 3: Archivo con formato corrupto (ParserError)
    # ---------------------------------------------------------
    print("\n[Prueba 3] Simulando archivo con formato corrupto (columnas irregulares)...")
    ruta_corrupta = "archivo_corrupto_temp.csv"
    
    # Creamos un archivo CSV mal formado (la segunda fila tiene más columnas que el encabezado)
    with open(ruta_corrupta, 'w') as f:
        f.write("Temperatura,Presion\n")
        f.write("20.5,100.2\n")
        f.write("21.0,101.5,dato_extra_invalido,colapsar_programa\n") 
        
    # Probamos la función
    datos_3 = cargar_datos(ruta_corrupta)
    assert datos_3 is None, "Error: La función debió retornar None."
    
    # Limpiamos el archivo temporal
    os.remove(ruta_corrupta)

    # ---------------------------------------------------------
    # RESULTADO FINAL
    # ---------------------------------------------------------
    print("\n" + "="*60)
    print(" PRUEBAS FINALIZADAS CON ÉXITO :) ")
    print(" El programa superó todos los errores sin detener su ejecución.")
    print("="*60)

if __name__ == "__main__":
    ejecutar_pruebas_qa()
