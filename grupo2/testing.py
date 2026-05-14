import numpy as np
import pandas as pd
from grupo2.estadisticas import calcular_estadisticas


def validar_estadisticas(datos: pd.DataFrame, tolerancia: float = 1e-6) -> bool:
    stats = calcular_estadisticas(datos)
    columnas_numericas = datos.select_dtypes(include=[np.number]).columns
    todos_ok = True

    for col in columnas_numericas:
        valores = datos[col].to_numpy()
        esperado = {
            "media": np.mean(valores),
            "std": np.std(valores),
            "max": np.max(valores),
            "min": np.min(valores),
        }
        for clave, valor_esperado in esperado.items():
            obtenido = stats[col][clave]
            if not np.isclose(obtenido, valor_esperado, atol=tolerancia):
                print(f"[FALLO] {col}.{clave}: esperado={valor_esperado:.6f}, obtenido={obtenido:.6f}")
                todos_ok = False

    if todos_ok:
        print("[OK] Todas las estadísticas son correctas.")
    return todos_ok



def generar_csvs_corruptos(carpeta: str = "grupo2/datos_prueba") -> None:
    import os
    os.makedirs(carpeta, exist_ok=True)

    with open(f"{carpeta}/vacio.csv", "w") as f:
        f.write("")

    with open(f"{carpeta}/sin_filas.csv", "w") as f:
        f.write("temperatura,presion\n")

    with open(f"{carpeta}/letras.csv", "w") as f:
        f.write("temperatura,presion\n")
        f.write("abc,xyz\n")
        f.write("100,200\n")

    with open(f"{carpeta}/columnas_incompletas.csv", "w") as f:
        f.write("temperatura,presion\n")
        f.write("100\n")
        f.write("200,300\n")

    df_ok = pd.DataFrame({
        "temperatura": np.random.normal(100, 5, 20),
        "presion": np.random.normal(50, 2, 20),
    })
    df_ok.to_csv(f"{carpeta}/correcto.csv", index=False)

    print(f"[OK] CSVs de prueba generados en '{carpeta}/'")


if __name__ == "__main__":
    print("=== Validación con datos de muestra ===")
    muestra = pd.DataFrame({
        "temperatura": [100.0, 102.0, 98.0, 101.0, 99.0],
        "presion":     [50.0,  51.0,  49.0, 50.5,  50.2],
    })
    validar_estadisticas(muestra)

    print("\n=== Generando CSVs corruptos ===")
    generar_csvs_corruptos()
