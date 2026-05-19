import os
from pathlib import Path

from grupo3.data_carga import cargar_datos
from grupo2.testing import generar_csvs_corruptos


def ejecutar_pruebas_qa():
    print("Pruebas de carga de datos\n")

    print("Archivo inexistente:")
    assert cargar_datos("ruta_inventada/datos_que_no_existen.csv") is None

    print("\nArchivo vacio:")
    ruta_vacia = "archivo_vacio_temp.csv"
    open(ruta_vacia, "w").close()
    assert cargar_datos(ruta_vacia) is None
    os.remove(ruta_vacia)

    print("\nCSV con columnas irregulares:")
    ruta_corrupta = "archivo_corrupto_temp.csv"
    with open(ruta_corrupta, "w") as f:
        f.write("Temperatura,Presion\n")
        f.write("20.5,100.2\n")
        f.write("21.0,101.5,extra,invalido\n")
    assert cargar_datos(ruta_corrupta) is None
    os.remove(ruta_corrupta)

    print("\nCSVs de prueba del grupo 2:")
    generar_csvs_corruptos()
    carpeta = Path("grupo2/datos_prueba")
    for ruta_csv in sorted(carpeta.glob("*.csv")):
        if ruta_csv.name == "correcto.csv":
            df_ok = cargar_datos(str(ruta_csv))
            assert df_ok is not None and not df_ok.empty
        else:
            assert cargar_datos(str(ruta_csv)) is None

    print("\nTodas las pruebas pasaron.")


if __name__ == "__main__":
    ejecutar_pruebas_qa()
